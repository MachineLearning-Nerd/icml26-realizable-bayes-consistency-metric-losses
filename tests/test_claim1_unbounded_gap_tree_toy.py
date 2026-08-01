import json
from pathlib import Path
from src.claim1_unbounded_gap_tree_toy import gap, run

def test_gap_is_increasing():
    assert [gap(k) for k in range(1,5)] == [8,32,128,512]

def test_paths_and_control(tmp_path: Path):
    r=run(4,tmp_path)
    assert r['paths_checked']==16 and r['all_paths_realizable']
    assert r['negative_control']['tree_extension_legal'] is False
    assert json.loads((tmp_path/'result.json').read_text())['metric']=='absolute_loss'
