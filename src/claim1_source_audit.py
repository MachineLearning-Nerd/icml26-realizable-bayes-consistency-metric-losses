"""Source-pinned local audit for Claim 1; no theorem verification asserted."""
from pathlib import Path
import tarfile,json
ROOT=Path(__file__).resolve().parents[1]
def source_text():
    with tarfile.open(ROOT/'evidence/source/arxiv_source.tar.gz','r:gz') as t:
        return t.extractfile('realizable_consistency_body.tex').read().decode('utf-8')
def audit():
    s=source_text()
    return {'source_member':'realizable_consistency_body.tex','has_unbounded_gap':'unbounded-gap Littlestone tree' in s,'has_characterization':'necessary and sufficient' in s,'scope':'Source-location audit only; not an independent proof or empirical reproduction.'}
if __name__=='__main__':
 o=ROOT/'outputs/claim1_source_audit.json';o.write_text(json.dumps(audit(),indent=2)+'\n');print(o)
