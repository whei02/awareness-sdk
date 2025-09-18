# Smoke test for pipeline if available
def test_pipeline_import():
    import importlib
    assert importlib.import_module("awareness_sdk")
