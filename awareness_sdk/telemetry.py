def track(event: str, props: dict | None = None):
    # No-op telemetry stub
    return {"event": event, "props": props or {}}
