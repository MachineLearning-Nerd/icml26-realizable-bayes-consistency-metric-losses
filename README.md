# Realizable Bayes-Consistency for General Metric Losses

Independent claim audit and clean-room reproduction workspace for:

> Dan Tsir Cohen, Steve Hanneke, and Aryeh Kontorovich, “Realizable Bayes-Consistency for General Metric Losses.”

Paper: [arXiv:2605.03823](https://arxiv.org/abs/2605.03823) · [HTML paper](https://arxiv.org/html/2605.03823) · [OpenReview record](https://openreview.net/forum?id=EmqsPzyNHh)

This is an independent reproduction/audit repository, not an author-maintained implementation. The pinned local source snapshot was retrieved on 2026-08-01. The current public arXiv record is v3 (2026-08-06) and notes acceptance to ICML 2026.

## Current status

**Overall: partial, toy-level evidence only.**

Machine-readable status labels are TOY and UNVERIFIED; neither label claims a
full theorem reproduction.

Claim 1 has a finite executable toy: a depth-8 source-aligned absolute-metric witness checks all 256 binary paths and a Lipschitz tree-free negative control. It supports the mechanics of the finite construction, not the paper’s infinite theorem or its necessary-and-sufficient characterization. Claims 2–5 have not been independently reproduced.

## Audit dossier

The standardized audit record is split into reviewable files:

- CLAIM_EVIDENCE.md maps each claim to its producer, evidence, status, and limitation.
- SOURCE_AUDIT.md pins the paper snapshot, contract, theorem anchors, and source-version boundary.
- BRANCH_AUDIT.md records the final branch map and commit attribution.
- ENVIRONMENT.md records the fixed local command, checksums, and compute boundary.
- REPORT.md states the scoped decision and what remains unverified.
- CITATION.cff and AUTHOR_THANK_YOU.md provide citation and author acknowledgement.
- EVIDENCE_MANIFEST.json content-addresses the dossier and source/evidence inputs.
- verify_final.py performs fail-closed checks on a local or fresh clone.

The dossier is a documentation and provenance publication. It does not
change the Claim 1 toy verdict or imply that Claims 2–5 have been reproduced.

| Paper claim | Repository status | What the evidence supports |
| --- | --- | --- |
| Theorem 4.5: characterization by absence of an infinite unbounded-gap Littlestone tree | **Toy only** | A finite depth-8 witness is executable; no infinite tree, compactness bridge, or consistency theorem is proved here. |
| Definition 4.1: infinite non-decreasing-`gamma_k` Littlestone trees | **Unverified** | The definition is pinned in `evidence/claim1_attempt1/tree_theorem_excerpt.tex`; no independent infinite construction is present. |
| Theorem 5.1: an infinite tree forces a learner-independent lower bound | **Unverified** | No independent distribution/risk lower-bound audit has been completed. |
| Theorem 6.5: no obstruction yields an explicit strongly universally consistent learner | **Unverified** | The constructive learner and its almost-sure risk proof have not been implemented or audited. |
| Section 3: finite `R*` is insufficient in general | **Unverified** | The paper source is pinned, but its counterexample has not been independently reproduced. |

The local contract was created from an earlier source snapshot and records the lower-bound claim as infinite expected risk. The current arXiv v3 abstract states the stronger almost-sure infinite-risk formulation. Neither formulation has been independently verified in this repository.

## What the paper does

The paper studies realizable strong universal Bayes-consistency when the label loss is a general metric and may be unbounded. It asks when a distribution-free learner can make risk converge almost surely to zero for every realizable distribution.

Its central obstruction is an **infinite non-decreasing-`gamma_k` Littlestone tree**: at depth `k`, the two possible labels at an instance are at least `gamma_k` apart, with `gamma_k` tending to infinity, while every finite labeling path remains realizable by the hypothesis class. Under the paper’s measurability and compact-parameterization assumptions, the main result says:

- an infinite unbounded-gap tree gives a lower bound ruling out strong universal consistency; and
- absence of such a tree gives an explicit distribution-free learner whose risk converges to zero almost surely.

The paper also gives a counterexample showing that a finite optimal risk condition alone does not characterize learnability for unbounded metric losses.

## How claims become evidence here

```text
pinned arXiv source + OpenReview contract
        -> claim list and source excerpts
        -> one scoped audit script per claim attempt
        -> JSON/CSV outputs plus checksums
        -> logbook entry and README verdict
```

For the completed Claim 1 attempt:

1. `evidence/source/` pins the paper PDF and source archive with SHA-256 checksums.
2. `evidence/claim1_attempt1/tree_theorem_excerpt.tex` records the relevant definitions and theorem statement.
3. `src/claim1_source_audit.py` checks that the pinned source contains the unbounded-gap tree and characterization language. This is a source-location audit, not a proof check.
4. `src/claim1_unbounded_gap_tree_toy.py` enumerates every finite binary path at depth 8, constructs the source-aligned independent-coordinate witness, measures absolute realization loss, and evaluates a Lipschitz negative control.
5. `outputs/claim1_unbounded_gap_tree_toy/result.json`, `paths.csv`, `run.log`, and `SHA256SUMS` are the machine-readable evidence.
6. `logbook/claim-1.md` records the method, result, scope, and verdict.

## Claim 1 evidence

The finite toy uses the Appendix Example 1 construction: absolute metric loss, labels `{0, 2^(2k+1)}`, and independent binary assignments on disjoint coordinates.

| Check | Result |
| --- | --- |
| Depth | 8 |
| Paths checked | 256 |
| All paths exactly realizable | Yes; maximum realization loss is 0 for every path |
| Gap sequence | 8, 32, 128, 512, 2048, 8192, 32768, 131072 |
| Negative control | For `L=3` Lipschitz functions after a fixed first label, the proposed depth-2 gap 32 exceeds the legal later gap 6 |
| Verdict | Finite constructive toy only |

This is evidence for the finite mechanics of the construction. It does not establish an infinite tree, a distributional lower bound, Theorem 4.5, or Bayes consistency.

## Repository contents

| Path | Purpose |
| --- | --- |
| `contract/metadata.json` | OpenReview and paper metadata |
| `contract/live_claims.json` | Five claims used by this audit |
| `contract/contract_manifest.json` | Retrieval metadata and source checksums |
| `evidence/source/` | Pinned arXiv PDF/source archive |
| `evidence/claim1_attempt1/` | Claim 1 source excerpt and checksum |
| `src/` | Reproduction and source-audit scripts |
| `outputs/` | Checked JSON/CSV results and checksums |
| `logbook/` | Claim-level audit notes |
| `STATUS.md` | Machine-readable project status summary |
| `AUTONOMOUS_STATE.json` | Handoff state for the next audit session |
| `branch-audit.md` | Branch and attribution audit |

No official executable code, dataset, or model checkpoint was identified in the pinned source archive. The reproduction therefore uses the paper’s stated construction and local CPU-only code. The compute policy is local CPU/local GPU only; no paid, remote, or Hugging Face Job compute is used.

## Reproduce the completed attempt

From the repository root:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/claim1_source_audit.py
.venv/bin/python src/claim1_unbounded_gap_tree_toy.py \
  --depth 8 \
  --out outputs/claim1_unbounded_gap_tree_toy
(cd outputs/claim1_unbounded_gap_tree_toy && sha256sum -c SHA256SUMS)
.venv/bin/python -m pytest -q
```

The output directory is intentionally tracked so that a reviewer can compare the generated result with the recorded evidence. Running the generator may update the interpreter/platform fields in `result.json` and `run.log`.

## Branch map

Only `main` exists. It contains the source-pinned workspace, the Claim 1 toy, its evidence, and this documentation. There are no historical `orx/*` branches or undocumented experiment branches in this repository. See [branch-audit.md](branch-audit.md) for the final branch and commit-attribution audit.

## Citation

```bibtex
@article{cohen2026realizable,
  title         = {Realizable Bayes-Consistency for General Metric Losses},
  author        = {Cohen, Dan Tsir and Hanneke, Steve and Kontorovich, Aryeh},
  journal       = {arXiv preprint arXiv:2605.03823},
  year          = {2026},
  doi           = {10.48550/arXiv.2605.03823}
}
```

Please cite the paper using the version and venue information preferred by the authors when available.

## Thank you

Thank you to Dan Tsir Cohen, Steve Hanneke, and Aryeh Kontorovich for making this work available and for developing a sharp, useful characterization of realizable learning under general metric losses. This repository is an independent reproduction and audit intended to make the paper’s claims, evidence boundaries, and remaining work easy to inspect.

## Limitations and next work

- The finite toy cannot replace the paper’s infinite combinatorial and measure-theoretic arguments.
- Claims 2–5 need separate, scoped audits with explicit evidence before they can be marked reproduced.
- The current code does not implement the paper’s general distribution-free learner.
- Results are CPU-local and are not a scaled replication of any unreported author experiment.

The next appropriate step is an independent audit of Claim 2’s infinite-tree definitions and the compact-parameterization bridge, while preserving the distinction between source inspection, finite numerical evidence, and theorem verification.
