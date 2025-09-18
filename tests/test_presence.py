from awareness_sdk.layers.presence import presence_inject

def test_presence_low_band_injects_breathing():
    text = "這是一段回應"
    out = presence_inject(text, freq={"band": "low"})
    assert "吸氣" in out or "呼吸" in out or "吐氣" in out

def test_presence_disabled():
    text = "這是一段回應"
    out = presence_inject(text, freq={"band": "high"}, cfg={"disable_presence": True})
    assert out == text
