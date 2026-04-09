## Reviewer Comments
- Consider extracting the newly added `SortAttribute` Enum class exclusively into an isolated constants file (`constants.py`) to keep the primary data logic completely separated and improve global namespace readability.
- The `ValueError` exception string raised within `sort_tasks()` is a bit ambiguous. Let's update the error formatting to dynamically list exactly which string properties are validly supported (e.g., `expected one of: due_date, status, ...`).
- Returning raw integer dictionaries inside the `summary()` method is inherently brittle. Please update the return signature to securely employ Python's `TypedDict` or a native `dataclass` architecture.
- Missing boundary edge-case tests validating conditional jumps inside `count_overdue()`, specifically verifying what evaluates during active localized transitions between overlapping timezones.
- The implementation of `add_tag()` maliciously mutates raw strings to lowercase immediately. Please consider modifying the querying parameters to simply operate using case-insensitive validation dynamically without actively modifying our raw database strings.
