# Environment and artifact record

## Fixed local command

From a clean checkout:

~~~text
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/claim1_source_audit.py
.venv/bin/python src/claim1_unbounded_gap_tree_toy.py --depth 8 --out outputs/claim1_unbounded_gap_tree_toy
(cd outputs/claim1_unbounded_gap_tree_toy && sha256sum -c SHA256SUMS)
.venv/bin/python -m pytest -q
~~~

The only declared dependency is pytest 8.3.5. The Claim 1 producer itself
uses the Python standard library. No Hugging Face Job, paid compute, remote
GPU, or author implementation is part of the evidence.

## Pinned inputs

| Input | SHA-256 |
| --- | --- |
| evidence/source/arxiv.pdf | de979b5ad57b35cfc2398a89f36728ea8ae865e62eedae46bfb8fb1c0055853b |
| evidence/source/arxiv_source.tar.gz | fe4b0fd95d2f695bd5475981c439a24fd5d7336dc11e2800e089a9ca1cdc83e4 |
| contract/contract_manifest.json | 6a1a5fab1f43c00ed344ab244b842c45279a7baef846115204dfaf231dda4455 |

## Claim 1 checkpoint

| Measurement | Recorded value |
| --- | --- |
| Depth | 8 |
| Binary paths | 256 |
| Gap sequence | 8, 32, 128, 512, 2048, 8192, 32768, 131072 |
| Metric | absolute loss |
| Realization result | all paths exactly realizable |
| Negative control | L=3, proposed gap 32, legal later gap 6, rejected |
| Hardware | local CPU; no remote run |

The tracked output records the interpreter and platform used by the historical
run. The dossier publication did not rerun the producer.

## Reproduction policy

- Label finite construction evidence as a toy, not a theorem proof.
- Keep source inspection, numerical construction, and measure-theoretic claims
  separate.
- Do not promote Claims 2–5 without a scoped producer, independent checker,
  raw output, and negative or boundary control.
