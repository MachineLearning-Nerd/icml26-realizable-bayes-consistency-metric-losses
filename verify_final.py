#!/usr/bin/env python3
"""Fail-closed structural checks for the realizable Bayes-consistency audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = (
    "MachineLearning-Nerd/"
    "icml26-realizable-bayes-consistency-metric-losses"
)
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = (
    "37579156+MachineLearning-Nerd@users.noreply.github.com"
)
EXPECTED_PDF_SHA = (
    "de979b5ad57b35cfc2398a89f36728ea8ae865e62eedae46bfb8fb1c0055853b"
)
EXPECTED_SOURCE_ARCHIVE_SHA = (
    "fe4b0fd95d2f695bd5475981c439a24fd5d7336dc11e2800e089a9ca1cdc83e4"
)
EXPECTED_CONTRACT_SHA = (
    "6a1a5fab1f43c00ed344ab244b842c45279a7baef846115204dfaf231dda4455"
)
EXPECTED_BRANCHES = {"main"}
EXPECTED_CLAIMS = {
    "C1": "TOY",
    "C2": "UNVERIFIED",
    "C3": "UNVERIFIED",
    "C4": "UNVERIFIED",
    "C5": "UNVERIFIED",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "BRANCH_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
    "AUTONOMOUS_STATE.json",
}
EXPECTED_AUDIT_FILES = REQUIRED_FILES - {"AUTONOMOUS_STATE.json"}
EXPECTED_EVIDENCE_FILES = {
    "contract/challenge_readme.md",
    "contract/metadata.json",
    "contract/live_claims.json",
    "contract/contract_manifest.json",
    "contract/claims_default_raw.json",
    "contract/claims_anchored_raw.json",
    "evidence/source/SHA256SUMS",
    "evidence/source/arxiv.pdf",
    "evidence/source/arxiv_source.tar.gz",
    "evidence/claim1_attempt1/SHA256SUMS",
    "evidence/claim1_attempt1/tree_theorem_excerpt.tex",
    "outputs/claim1_source_audit.json",
    "outputs/claim1_unbounded_gap_tree_toy/result.json",
    "outputs/claim1_unbounded_gap_tree_toy/paths.csv",
    "outputs/claim1_unbounded_gap_tree_toy/run.log",
    "outputs/claim1_unbounded_gap_tree_toy/SHA256SUMS",
    "src/claim1_source_audit.py",
    "src/claim1_unbounded_gap_tree_toy.py",
    "tests/test_claim1_unbounded_gap_tree_toy.py",
    "tests/test_contract.py",
    "logbook/claim-1.md",
    "requirements.txt",
}
EXPECTED_EVIDENCE_DIRS = {
    "contract",
    "evidence/source",
    "evidence/claim1_attempt1",
    "outputs/claim1_unbounded_gap_tree_toy",
    "src",
    "tests",
    "logbook",
}
CONTENT_ADDRESSED_PATHS = {
    *EXPECTED_AUDIT_FILES - {"EVIDENCE_MANIFEST.json"},
    "branch-audit.md",
    *EXPECTED_EVIDENCE_FILES,
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def read_json(relative_path: str) -> object:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(relative_path: str) -> str:
    digest = hashlib.sha256()
    with (ROOT / relative_path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_branches() -> set[str]:
    refs = run(
        "git",
        "for-each-ref",
        "refs/heads",
        "--format=%(refname:strip=2)",
    )
    return {ref.strip() for ref in refs.splitlines() if ref.strip()}


def remote_branches() -> set[str]:
    prefix = "refs/remotes/origin/"
    refs = run(
        "git",
        "for-each-ref",
        "refs/remotes/origin",
        "--format=%(refname)",
    )
    return {
        ref.strip()[len(prefix):]
        for ref in refs.splitlines()
        if ref.strip().startswith(prefix)
        and ref.strip() != prefix + "HEAD"
    }


def verify_remote() -> None:
    remote = run("git", "config", "--get", "remote.origin.url").strip()
    normalized = remote.removesuffix(".git").rstrip("/")
    if not normalized.endswith(EXPECTED_REPOSITORY):
        fail(f"origin is {remote!r}, expected {EXPECTED_REPOSITORY!r}")


def verify_branch_tips() -> None:
    if remote_branches() != EXPECTED_BRANCHES:
        fail(f"remote branch set is {sorted(remote_branches())!r}")
    local = local_branches()
    if "main" not in local:
        fail("local main branch is missing")
    remote_tip = run(
        "git",
        "rev-parse",
        "refs/remotes/origin/main",
    ).strip()
    local_tip = run("git", "rev-parse", "refs/heads/main").strip()
    if local_tip != remote_tip:
        fail("local main and origin/main tips differ")
    head = run("git", "symbolic-ref", "refs/remotes/origin/HEAD").strip()
    if head != "refs/remotes/origin/main":
        fail(f"origin HEAD is {head!r}, expected origin/main")


def verify_history() -> None:
    records = run(
        "git",
        "log",
        "--all",
        "--format=%an%x00%ae%x00%cn%x00%ce",
    ).splitlines()
    if not records:
        fail("no reachable commits")
    expected = (
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}\x00"
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}"
    )
    unexpected = sorted({record for record in records if record != expected})
    if unexpected:
        fail(f"non-canonical reachable identities: {unexpected}")
    if "co-authored-by:" in run("git", "log", "--all", "--format=%B").lower():
        fail("co-author trailer found")
    if int(run("git", "rev-list", "--count", "--all").strip()) < 8:
        fail("historical evidence commits are missing")
    if run(
        "git",
        "for-each-ref",
        "refs/original",
        "--format=%(refname)",
    ).strip():
        fail("temporary refs/original remain")
    refs = run("git", "for-each-ref", "--format=%(refname)").splitlines()
    if any("orx/" in ref or ref.endswith("/orx") for ref in refs):
        fail("legacy orx ref remains")


def verify_manifest() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    if not isinstance(manifest, dict):
        fail("manifest must be a JSON object")
    if manifest.get("repository") != EXPECTED_REPOSITORY:
        fail("manifest repository marker is wrong")
    if manifest.get("claim_statuses") != EXPECTED_CLAIMS:
        fail("manifest claim statuses are wrong")
    if set(manifest.get("required_audit_files", [])) != EXPECTED_AUDIT_FILES:
        fail("manifest audit-file list is wrong")
    if set(manifest.get("required_evidence_files", [])) != EXPECTED_EVIDENCE_FILES:
        fail("manifest evidence-file list is wrong")
    if set(manifest.get("required_evidence_directories", [])) != EXPECTED_EVIDENCE_DIRS:
        fail("manifest evidence-directory list is wrong")
    branches = manifest.get("branches", {})
    if set(branches.get("expected_final", [])) != EXPECTED_BRANCHES:
        fail("manifest branch set is wrong")
    if branches.get("historical_remote_branch_count") != 1:
        fail("manifest historical branch count is wrong")
    if branches.get("legacy_prefixes_removed") != ["orx/"]:
        fail("manifest legacy-prefix record is wrong")
    if manifest.get("attribution", {}).get("email") != CANONICAL_EMAIL:
        fail("manifest attribution is wrong")
    artifacts = manifest.get("content_addressed_artifacts", [])
    if {item.get("path") for item in artifacts} != CONTENT_ADDRESSED_PATHS:
        fail("manifest content-addressed path list is wrong")
    for item in artifacts:
        relative_path = item.get("path")
        expected_hash = item.get("sha256")
        if not isinstance(relative_path, str) or not isinstance(expected_hash, str):
            fail("malformed content-addressed artifact")
        if not (ROOT / relative_path).is_file():
            fail(f"missing content-addressed artifact: {relative_path}")
        if sha256(relative_path) != expected_hash:
            fail(f"artifact hash mismatch: {relative_path}")


def verify_checksum_file(relative_path: str, base: str) -> None:
    for line in (ROOT / relative_path).read_text(encoding="utf-8").splitlines():
        expected_hash, filename = line.split()
        candidate = str(Path(base) / filename)
        if sha256(candidate) != expected_hash:
            fail(f"checksum mismatch in {relative_path}: {filename}")


def verify_evidence() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    for relative_path in manifest.get("required_evidence_files", []):
        if not (ROOT / relative_path).is_file():
            fail(f"missing required evidence file: {relative_path}")
    for relative_path in manifest.get("required_evidence_directories", []):
        if not (ROOT / relative_path).is_dir():
            fail(f"missing required evidence directory: {relative_path}")

    verify_checksum_file("evidence/source/SHA256SUMS", "evidence/source")
    verify_checksum_file(
        "evidence/claim1_attempt1/SHA256SUMS",
        "evidence/claim1_attempt1",
    )
    verify_checksum_file(
        "outputs/claim1_unbounded_gap_tree_toy/SHA256SUMS",
        "outputs/claim1_unbounded_gap_tree_toy",
    )

    contract = read_json("contract/contract_manifest.json")
    if contract.get("claim_count") != 5 or contract.get("maximum_points") != 10:
        fail("contract count or maximum points are wrong")
    if contract.get("openreview_id") != "EmqsPzyNHh":
        fail("contract OpenReview ID is wrong")
    if contract.get("sha256", {}).get("evidence/source/arxiv.pdf") != EXPECTED_PDF_SHA:
        fail("contract PDF hash is wrong")
    if contract.get("sha256", {}).get("evidence/source/arxiv_source.tar.gz") != EXPECTED_SOURCE_ARCHIVE_SHA:
        fail("contract source archive hash is wrong")

    source_audit = read_json("outputs/claim1_source_audit.json")
    if (
        source_audit.get("source_member") != "realizable_consistency_body.tex"
        or source_audit.get("has_unbounded_gap") is not True
        or source_audit.get("has_characterization") is not True
    ):
        fail("source-location audit is wrong")

    result = read_json("outputs/claim1_unbounded_gap_tree_toy/result.json")
    expected_gaps = [8, 32, 128, 512, 2048, 8192, 32768, 131072]
    if (
        result.get("kind") != "reduced_finite_depth_tree_toy"
        or result.get("depth") != 8
        or result.get("paths_checked") != 256
        or result.get("gamma_sequence") != expected_gaps
        or result.get("metric") != "absolute_loss"
        or result.get("all_paths_realizable") is not True
    ):
        fail("Claim 1 toy result is wrong")
    control = result.get("negative_control", {})
    if (
        control.get("L") != 3
        or control.get("max_later_legal_gap") != 6
        or control.get("proposed_depth2_gap") != 32
        or control.get("tree_extension_legal") is not False
    ):
        fail("Claim 1 negative control is wrong")
    if "not an infinite-tree" not in result.get("scope", ""):
        fail("Claim 1 scope boundary is missing")

    if len((ROOT / "outputs/claim1_unbounded_gap_tree_toy/paths.csv").read_text().splitlines()) != 257:
        fail("Claim 1 path count is wrong")
    live_claims = read_json("contract/live_claims.json")
    if len(live_claims) != 5 or any(item.get("status") != "unverified" for item in live_claims):
        fail("live claim contract is not the expected five-claim boundary")
    if "Theorem 4.5" not in live_claims[0].get("text", ""):
        fail("Claim 1 anchor is missing")


def verify_ledgers_and_state() -> None:
    claims = read_json("claims.json")
    state = read_json("AUTONOMOUS_STATE.json")
    if not isinstance(claims, dict) or not isinstance(state, dict):
        fail("claim ledger and state must be JSON objects")
    if {
        row.get("id"): row.get("status") for row in claims.get("claims", [])
    } != EXPECTED_CLAIMS:
        fail("claims.json statuses are wrong")
    if claims.get("repository") != EXPECTED_REPOSITORY:
        fail("claims.json repository marker is wrong")
    paper = claims.get("paper", {})
    if paper.get("pdf_sha256") != EXPECTED_PDF_SHA:
        fail("claims.json PDF source hash is wrong")
    if paper.get("source_archive_sha256") != EXPECTED_SOURCE_ARCHIVE_SHA:
        fail("claims.json source archive hash is wrong")
    if state.get("github_repository") != "https://github.com/" + EXPECTED_REPOSITORY:
        fail("state repository marker is wrong")
    if state.get("canonical_branch") != "main":
        fail("state canonical branch is wrong")
    if set(state.get("expected_branches", [])) != EXPECTED_BRANCHES:
        fail("state branch set is wrong")
    if state.get("historical_branch_count") != 0:
        fail("state historical branch count is wrong")
    if state.get("paper_pdf_sha256") != EXPECTED_PDF_SHA:
        fail("state PDF source hash is wrong")
    if state.get("paper_source_archive_sha256") != EXPECTED_SOURCE_ARCHIVE_SHA:
        fail("state source archive hash is wrong")
    if state.get("contract_manifest_sha256") != EXPECTED_CONTRACT_SHA:
        fail("state contract hash is wrong")
    identity = state.get("canonical_identity", {})
    if identity.get("name") != CANONICAL_NAME or identity.get("email") != CANONICAL_EMAIL:
        fail("state canonical identity is wrong")
    if state.get("phase") not in {
        "dossier_ready_for_publication",
        "dossier_published_claim_1_toy_only",
    }:
        fail("state phase is not a dossier phase")


def verify_documentation() -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            fail(f"required file is missing: {relative_path}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "EVIDENCE_MANIFEST.json",
        "TOY",
        "Unverified",
        "verify_final.py",
    ):
        if marker not in readme:
            fail(f"README is missing marker {marker!r}")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    for marker in (
        "dossier_published_claim_1_toy_only",
        "Evidence boundary",
        "Verification status",
    ):
        if marker not in status:
            fail(f"STATUS is missing marker {marker!r}")
    branch_audit = (ROOT / "BRANCH_AUDIT.md").read_text(encoding="utf-8")
    if "main" not in branch_audit or "MachineLearning-Nerd" not in branch_audit:
        fail("branch audit is incomplete")
    if "ORX" not in branch_audit:
        fail("branch audit legacy-prefix boundary is missing")
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text(encoding="utf-8")
    for source_hash in (EXPECTED_PDF_SHA, EXPECTED_SOURCE_ARCHIVE_SHA, EXPECTED_CONTRACT_SHA):
        if source_hash not in source_audit:
            fail("source audit hash is missing")
    thanks = (ROOT / "AUTHOR_THANK_YOU.md").read_text(encoding="utf-8")
    for author in ("Dan Tsir Cohen", "Steve Hanneke", "Aryeh Kontorovich"):
        if author not in thanks:
            fail(f"author thanks is missing {author}")


def main() -> int:
    verify_documentation()
    verify_remote()
    verify_branch_tips()
    verify_history()
    verify_manifest()
    verify_evidence()
    verify_ledgers_and_state()
    print("PASS: published realizable Bayes-consistency audit state is structurally verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
