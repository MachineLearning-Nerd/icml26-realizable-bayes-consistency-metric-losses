# Claim 1 — necessary/sufficient characterization

**Exact live claim:** Theorem 4.5 gives a necessary and sufficient condition for realizable strong universal Bayes-consistency with general metric losses, characterized via an unbounded-gap Littlestone tree obstruction (Section 4, Theorem 4.5).

## Local direct constructive toy

The pinned source defines a non-decreasing-gap Littlestone tree as a full binary tree whose outgoing labels have metric gap at least `gamma_k`, with every finite path realized by a hypothesis (`evidence/claim1_attempt1/tree_theorem_excerpt.tex`). Its appendix example uses disjoint intervals, absolute loss, and labels `{0, 2^(2k+1)}`.

`src/claim1_unbounded_gap_tree_toy.py` executes that construction at finite depth 8: it enumerates all 256 binary paths, builds the corresponding independent-coordinate hypothesis, and measures absolute realization loss. **Result:** 256/256 paths have maximum loss 0, while gaps are `[8, 32, 128, 512, 2048, 8192, 32768, 131072]`.

**Negative control:** after a first fixed label, an `L=3` Lipschitz class on `[0,1]` permits later label gaps no larger than `2L=6`; the proposed depth-2 gap 32 is rejected. This operationalizes the paper's contrasting tree-free example.

```bash
.venv/bin/python src/claim1_unbounded_gap_tree_toy.py --depth 8 --out outputs/claim1_unbounded_gap_tree_toy
(cd outputs/claim1_unbounded_gap_tree_toy && sha256sum -c SHA256SUMS)
.venv/bin/python -m pytest -q
```

**Verdict: toy.** This is an executable finite-depth witness and destructive control using the source metric/construction. It does **not** prove the infinite obstruction, either direction of Theorem 4.5, or universal Bayes consistency.
