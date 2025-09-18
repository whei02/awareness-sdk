def ensure_text(s):
    if not isinstance(s, str) or not s.strip():
        raise ValueError("input text required")
    return s.strip()
