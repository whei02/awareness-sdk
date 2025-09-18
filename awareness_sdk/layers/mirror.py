def mirror_reply(text: str, locale: str = "zh-TW") -> str:
    """
    最簡鏡映：抓住情緒詞或直接承接用語。
    """
    if locale.startswith("zh"):
        return f"我聽見你說：「{text}」。"
    return f"I hear you said: “{text}”."
