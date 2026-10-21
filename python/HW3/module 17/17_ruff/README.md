# Ruff Exercise

## Original Ruff Violations

- E401 - Multiple imports on one line. Fixed by splitting the imports.
- I001 - Import block was unsorted. Fixed by organizing the imports.
- F401 - Unused imports (`os`, `sys`, `json`). Fixed by removing them.
- N802 - Function name `Add` was not lowercase. Fixed by renaming it to `add`.
- F841 - Variables `unused` and `msg` were assigned but never used. Fixed by removing them.
- F541 - F-string had no placeholders. Ruff removed the unnecessary `f` prefix.
- E711 - Used `== None`. Fixed manually by changing it to `is None`.
- Q000 - Single quotes were used instead of double quotes. Fixed by changing them to double quotes.
- W292 - File had no newline at the end. Fixed by adding a final newline.

## Final Checks

`ruff check .`

All checks passed!

`ruff format --check .`

1 file already formatted