# Claim-to-evidence map

The repository’s production graph is:

    pinned source and contract -> scoped claim contract
        -> executable producer -> committed output/checksum
        -> limitation and verdict

Only Claim 1 currently reaches the executable-producer stage. Claims 2–5 are
documented as unverified rather than represented by guessed experiments.

## Evidence boundary

- The paper contract is in contract/live_claims.json; retrieval metadata and
  source checksums are in contract/contract_manifest.json.
- evidence/source/ pins the PDF and LaTeX source archive. The source snapshot
  was retrieved on 2026-08-01; the public arXiv record later moved to v3.
- Claim 1 has a source-location audit, a finite depth-8 construction, a
  negative control, JSON/CSV outputs, run log, and checksums.
- Claims 2–5 have no independent producer, checker, raw result, or verdict
  beyond the unverified contract entries. No toy is substituted for them.
- No official executable implementation, dataset, checkpoint, external
  compute run, judge score, or author endorsement is claimed.

## C1 — Theorem 4.5 characterization

Paper anchor: Section 4, Theorem 4.5.

Producer path:

1. src/claim1_source_audit.py checks that the pinned source contains the
   unbounded-gap Littlestone-tree and necessary-and-sufficient
   characterization language.
2. src/claim1_unbounded_gap_tree_toy.py implements the Appendix Example 1
   construction at finite depth 8 under absolute metric loss.
3. The producer enumerates all 256 binary paths, assigns independent
   coordinates, and records exact realization loss and the gap sequence.
4. A fixed first-label L=3 Lipschitz control rejects the proposed later gap
   32 because the legal gap is at most 6.
5. outputs/claim1_unbounded_gap_tree_toy/ contains result.json, paths.csv,
   run.log, and SHA256SUMS.

Observed result: all 256 paths are exactly realizable; gaps are
8, 32, 128, 512, 2048, 8192, 32768, and 131072; the Lipschitz control rejects
the depth-2 extension.

Verdict: **TOY**. This supports finite construction mechanics only. It does
not prove an infinite tree, the compactness bridge, the lower-bound direction,
or the necessary-and-sufficient theorem.

## C2 — Definition 4.1: infinite non-decreasing-gap trees

Paper anchor: Section 4, Definition 4.1.

No independent producer or checker has been committed. The next audit must
formalize the quantifiers over an infinite full binary tree, non-decreasing
gamma_k, diverging gaps, realizability of every finite path, and the
relationship between the source definition and the finite toy.

Verdict: **UNVERIFIED**.

## C3 — Theorem 5.1: learner-independent lower bound

Paper anchor: Section 5, Theorem 5.1.

No distributional construction, risk calculation, or learner-independent
lower-bound checker has been committed. The local contract records an
expected-risk formulation, while the later public abstract uses an
almost-sure infinite-risk formulation; that version boundary must be settled
before an audit is scored.

Verdict: **UNVERIFIED**.

## C4 — Theorem 6.5: explicit consistent learner

Paper anchor: Section 6, Theorem 6.5.

No implementation of the distribution-free learner, compact
parameterization, measurability argument, or almost-sure risk proof has been
committed. A future audit must keep numerical checks separate from the
theorem’s measure-theoretic conclusion.

Verdict: **UNVERIFIED**.

## C5 — Section 3 finite-optimal-risk counterexample

Paper anchor: Section 3 and the paper’s counterexample showing finite R*
is insufficient.

No independent counterexample construction or risk comparison has been
committed. The pinned source is available for a separate finite audit.

Verdict: **UNVERIFIED**.

## Reproduction boundary

The fixed local Claim 1 command is recorded in ENVIRONMENT.md. Re-running
the generator can change interpreter/platform fields in the tracked output;
such a rerun must update the output checksum and this dossier together.
