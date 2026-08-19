# Audit report

## Decision

**PARTIAL_TOY_ONLY**

The repository provides a finite depth-8 construction aligned with the
paper’s Appendix Example 1 and a Lipschitz tree-free negative control. This is
useful evidence for the mechanics of the construction, but it is not a
reproduction of the infinite characterization theorem.

Machine-readable overall verdict: PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_5_UNVERIFIED.
The publication boundary is publication_allowed=false for a complete
reproduction or score; score_claim=false and
official_author_endorsement=false.

## Claim decisions

- C1 is **TOY**: 256/256 finite paths are exactly realizable and the
  Lipschitz control rejects the proposed extension.
- C2 is **UNVERIFIED**: no infinite-tree definition audit is committed.
- C3 is **UNVERIFIED**: no learner-independent lower-bound construction is
  committed.
- C4 is **UNVERIFIED**: no explicit learner or almost-sure risk audit is
  committed.
- C5 is **UNVERIFIED**: no independent finite-optimal-risk counterexample is
  committed.

## Evaluation boundary

No judge score, external logbook score, official author implementation, or
author endorsement is claimed. The source snapshot and local output checksums
are the reproducibility boundary. The public arXiv v3 note is disclosed as
source-version context, not used to rewrite the pinned evidence.

## Publication state

The repository uses the canonical
icml26-realizable-bayes-consistency-metric-losses name, a single documented
main branch, canonical MachineLearning-Nerd attribution, a claim-to-evidence
dossier, machine-readable verdicts/state, citation, author thanks, content
manifest, and fail-closed verifier.
