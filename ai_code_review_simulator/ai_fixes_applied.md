# AI Fixes Applied

| AI Suggestion                                | Action Taken     | Notes                    |
|----------------------------------------------|------------------|--------------------------|
| Add input sanitization to escape malicious HTML tags from `title` and `description` | ❌ Rejected      | Justification: Over-engineering. Security escaping is a presentation-layer concern and should be handled exclusively by the frontend. |
| Explicitly add documentation regarding tag formatting rules in `add_tag(tag)` | ✅ Applied       | Justification: Adding explicitly documented behavior inside the docstring enforcing lowercase conversion improves the API contract constraints. |
| Employ timezone-aware tracking prior to using `isoformat()` | ✅ Applied       | Justification: Implementing `datetime.now(timezone.utc)` removes global tracking configuration faults across different deployment regions. |
| Avoid blindly trusting `uuid.uuid4()` unconditionally if task references function as secure access URLs | ❌ Rejected      | Justification: `uuid4` acts strictly as an internal memory identification key schema rather than a cryptographic authentication token, rendering replacement unnecessary. |
| Simplify `filter_tasks()` consecutive list comprehensions evaluating locally constructed variable iterations to fix O(N * K) complexity | ✅ Applied       | Justification: Flattens the array generator into a uniform single-pass $O(N)$ execution dynamically skipping unused loops. |
| Leverage a formal `Enum` class framework for `sort_tasks` to strictly clamp approved domains of sort inputs | ✅ Applied       | Justification: Instantiates `SortAttribute` to definitively categorize properties, shielding the function from brittle string validation. |
| Instantiate native metric iterators or caching mechanisms in `summary()` to avoid looping through database records repeatedly | ✅ Applied       | Justification: Rerouted iteration strictly across `self.tasks` entirely a single time natively generating independent value clusters natively matching outputs. |
| Introduce a lightweight `count_overdue()` iterator resolving directly without overhead array construction | ✅ Applied       | Justification: Abstracted the boundary query formally into `count_overdue` leveraging generator summation to natively eliminate external structural tracking overhead loops. |
