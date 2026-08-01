import json,hashlib
from pathlib import Path
from src.claim1_source_audit import audit
R=Path(__file__).resolve().parents[1]
def test_contract():
 d=json.loads((R/'contract/contract_manifest.json').read_text()); assert d['claim_count']==5 and d['maximum_points']==10; assert len(json.loads((R/'contract/live_claims.json').read_text()))==5
def test_source_and_audit():
 for line in (R/'evidence/source/SHA256SUMS').read_text().splitlines():
  h,n=line.split(); assert hashlib.sha256((R/'evidence/source'/n).read_bytes()).hexdigest()==h
 a=audit();assert a['has_unbounded_gap'] and a['has_characterization']
