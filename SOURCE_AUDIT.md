# Source audit

## Paper identity

| Field | Record |
| --- | --- |
| Title | Realizable Bayes-Consistency for General Metric Losses |
| Authors | Dan Tsir Cohen; Steve Hanneke; Aryeh Kontorovich |
| Primary source | arXiv:2605.03823 |
| OpenReview record | EmqsPzyNHh |
| Venue record | ICML 2026 |
| Pinned source retrieval | 2026-08-01 |
| Public record note | arXiv v3 is dated 2026-08-06; this audit does not silently replace the pinned snapshot |
| PDF SHA-256 | de979b5ad57b35cfc2398a89f36728ea8ae865e62eedae46bfb8fb1c0055853b |
| LaTeX source archive SHA-256 | fe4b0fd95d2f695bd5475981c439a24fd5d7336dc11e2800e089a9ca1cdc83e4 |
| Contract manifest SHA-256 | 6a1a5fab1f43c00ed344ab244b842c45279a7baef846115204dfaf231dda4455 |

The exact local inputs are evidence/source/arxiv.pdf and
evidence/source/arxiv_source.tar.gz. The source member used for the Claim 1
location audit is realizable_consistency_body.tex.

## Claim anchors

| Claim | Source anchor | Local scope |
| --- | --- | --- |
| C1 | Section 4, Theorem 4.5 | Finite Appendix Example 1 construction only; theorem remains unproved. |
| C2 | Section 4, Definition 4.1 | Definition and infinite-quantifier audit not started. |
| C3 | Section 5, Theorem 5.1 | Lower-bound and risk-formulation audit not started. |
| C4 | Section 6, Theorem 6.5 | Learner and almost-sure convergence audit not started. |
| C5 | Section 3 counterexample | Finite R* insufficiency audit not started. |

The claim text used for this workspace is preserved in
contract/live_claims.json. The contract’s earlier expected-risk wording and
the later public almost-sure abstract wording are both disclosed rather than
merged into one unverified claim.

## Implementation status

No author executable implementation, dataset, or checkpoint was identified
in the pinned source archive. This repository contains an independent source
audit and finite constructive toy, not an official reproduction package.

## Repository identity

- Former repository:
  MachineLearning-Nerd/icml26-repro-EmqsPzyNHh-realizable-bayes-consistency-metric-losses
- Canonical repository:
  MachineLearning-Nerd/icml26-realizable-bayes-consistency-metric-losses
- Canonical branch: main
- Repository homepage: https://arxiv.org/abs/2605.03823
