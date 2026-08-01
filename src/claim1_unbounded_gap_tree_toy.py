#!/usr/bin/env python3
"""Finite executable witness for the paper's unbounded-gap tree example.
Reduced finite-depth toy; it cannot establish the infinite theorem."""
from __future__ import annotations
import argparse, csv, hashlib, json, platform, sys
from itertools import product
from pathlib import Path


def gap(k: int) -> int:
    # Appendix Example 1: labels {0,2^(2k+1)} under absolute metric loss.
    return 2 ** (2 * k + 1)


def run(depth: int, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    all_realizable = True
    for bits in product((0, 1), repeat=depth):
        # H permits independent binary assignments on disjoint I_k.
        hypothesis = {k: (gap(k) if bit else 0) for k, bit in enumerate(bits, 1)}
        labels = [hypothesis[k] for k in range(1, depth + 1)]
        loss = [abs(hypothesis[k] - labels[k - 1]) for k in range(1, depth + 1)]
        realized = max(loss) == 0
        all_realizable &= realized
        rows.append({"path": "".join(map(str,bits)), "max_realization_loss": max(loss), "realized": realized})
    # Negative control: after one L-Lipschitz choice on [0,1], all later
    # compatible values are within L; proposed gap gamma_2=32 exceeds 2L.
    L = 3
    proposed_gap = gap(2)
    lipschitz_legal = proposed_gap <= 2 * L
    result = {
        "kind": "reduced_finite_depth_tree_toy",
        "depth": depth,
        "paths_checked": len(rows),
        "gamma_sequence": [gap(k) for k in range(1, depth + 1)],
        "metric": "absolute_loss",
        "all_paths_realizable": all_realizable,
        "negative_control": {
            "class": "L-Lipschitz functions on [0,1] after fixed first label",
            "L": L, "max_later_legal_gap": 2 * L,
            "proposed_depth2_gap": proposed_gap,
            "tree_extension_legal": lipschitz_legal,
        },
        "scope": "Finite executable version of the paper Appendix Example 1; not an infinite-tree or Bayes-consistency proof.",
        "python": sys.version, "platform": platform.platform(),
    }
    with (out / "paths.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    return result

if __name__ == "__main__":
    p=argparse.ArgumentParser(); p.add_argument("--depth",type=int,default=8); p.add_argument("--out",type=Path,required=True)
    a=p.parse_args(); print(json.dumps(run(a.depth,a.out),indent=2))
