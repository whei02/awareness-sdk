# Contributing

Thanks for helping improve Awareness SDK!

## Environment & Install
- Python ≥ 3.9
- Create a virtual environment and install dev deps:
  ```bash
  python -m venv .venv
  # Windows: .venv\Scripts\activate
  pip install -e ".[dev]"
  python -m pytest -q
  ```

## Coding Style
- Follow PEP 8; prefer type hints.
- Keep PRs focused and small.
- Add/adjust tests for behavior changes in `tests/`.
- Update README/examples when public API or CLI changes.

## Testing
- Unit tests must pass locally and in CI: `python -m pytest -q`.
- Avoid real network calls in tests; use stubs/fallbacks.

## CLI
- Keep backwards compatibility when possible.
- Document new flags in README and examples.

## Security
- Never commit secrets or API keys.
- Use GitHub Actions Secrets for CI secrets.

## Making a PR
1. Fork or branch off `main`.
2. Commit messages using Conventional Commits (e.g., `feat:`, `fix:`, `docs:`, `test:`, `ci:`).
3. Open a PR and fill out the template.
4. Ensure CI passes and respond to reviews.
