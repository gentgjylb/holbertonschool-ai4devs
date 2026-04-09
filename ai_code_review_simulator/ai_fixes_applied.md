# AI Fixes Applied Log

| AI Suggestion | Action Taken | Justification |
| :--- | :--- | :--- |
| Add HTML input sanitization for `title` and `description` | ❌ Rejected | Security escaping belongs firmly at the presentation layer; polluting base data models breaks standard separation of concerns. |
| Explicitly document implicit lowercase conversion executed in `add_tag()` | ✅ Applied | Eliminates ambiguity inside the API contract and enforces predictable tagging expectations. |
| Utilize timezone-aware date markers across `datetime.now()` instantiation | ✅ Applied | Establishes a predictable universal state (`timezone.utc`) effectively eliminating multi-region inconsistencies. |
| Re-evaluate `uuid.uuid4()` string generation for cryptographical security | ❌ Rejected | UUID is functioning cleanly as an internal mapping identifier and is fundamentally isolated from secure-access tokenizing workflows so replacing it provides zero benefit. |
| Flatten chained `filter_tasks()` list comprehensions into a combined loop pass | ✅ Applied | Systematically collapses the pipeline complexity down from `O(N * K)` to a single high-performance `O(N)` constraint matrix. |
| Extract hardcoded sorting configuration inputs into a strictly typed `Enum` | ✅ Applied | Employs `SortAttribute(Enum)` clamping downstream execution logic exclusively to valid parameters, eliminating brittle dictionary errors. |
| Optimize `summary()` data extraction loops to prevent unnecessary allocations | ✅ Applied | Iterating exactly once sequentially aggregates `completed`, `pending`, and `overdue` states automatically avoiding triple iterations across the main array. |
| Completely decouple main filtering logic into a Fluent Query Builder architecture | ❌ Rejected | Substantial over-engineering (`YAGNI`) for an object designed exclusively for localized management workflows. |
