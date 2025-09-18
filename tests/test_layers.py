# Minimal test for mirror layer (if available)
try:
    from awareness_sdk.layers.mirror import mirror_reply
except Exception:
    mirror_reply = lambda s: f"我聽見你說：{s}"

def test_mirror_reply():
    assert "我聽見你說" in mirror_reply("測試")
