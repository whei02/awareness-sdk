import pytest
from awareness_sdk.layers.frequency import detect_frequency

def test_detect_low_frequency():
    res = detect_frequency("我很焦慮，也很擔心未來。")
    assert res["band"] == "low"
    assert res["score"] < 200
    assert any(cue in ["焦慮", "擔心"] for cue in res["cues"])

def test_detect_high_frequency():
    res = detect_frequency("充滿喜悅與感謝，超級興奮！")
    assert res["band"] == "high"
    assert res["score"] > 400
    assert any(cue in ["喜悅", "感謝", "興奮"] for cue in res["cues"])

from awareness_sdk.pipeline import AwarenessPipeline
from awareness_sdk.integrations.openai_client import OpenAIChat

def test_pipeline_basic_response_offline():
    # 不需要 OpenAI 金鑰也能跑，會自動走規則式後備
    llm = OpenAIChat(model="gpt-4o-mini", temperature=0.0)
    asp = AwarenessPipeline(llm=llm, config={"disable_presence": True})
    resp = asp.respond("我好焦慮，怕換工作失敗。", metadata={"locale": "zh-TW"})

    # 回應文字存在
    assert isinstance(resp.text, str) and len(resp.text) > 0

    # Meta 結構齊全
    meta = resp.meta
    assert "labels" in meta and "phases" in meta
    assert "frequency" in meta["labels"]
    assert meta["labels"]["frequency"]["band"] in {"low", "mid", "high"}

    # 鏡映階段存在
    assert "mirror" in meta["phases"]
    assert "我聽見你說" in meta["phases"]["mirror"]

