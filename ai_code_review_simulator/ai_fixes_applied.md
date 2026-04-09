# AI Fixes Applied

| AI Suggestion | Action Taken | Notes |
|----------------------------------------------|------------------|--------------------------|
| Add input sanitization to escape malicious HTML tags from `title` and `description` | ❌ Rejected | Over-engineering for a local model. Security escaping is a presentation-layer concern and should be handled by the frontend, not the backend storage class. |
| Explicitly add documentation regarding tag formatting rules in `add_tag(tag)` | ✅ Applied | Added explicitly documented behavior in the method docstring indicating tags are forced to lowercase. |
| Employ timezone-aware tracking prior to using `isoformat()` | ✅ Applied | Replaced `datetime.now()` with `datetime.now(timezone.utc)` to ensure time formats scale safely across global configurations. |
| Avoid blindly trusting `uuid.uuid4()` unconditionally if task references function as secure access URLs | ❌ Rejected | `uuid4` is exclusively used as an internal primary key/identifier, not as an authentication/secure access token, making the fix unnecessary. |
| Simplify `filter_tasks()` consecutive list comprehensions evaluating locally constructed variable iterations to fix O(N * K) complexity | ✅ Applied | Flattened the multiple sequential list comprehensions into a single loop mapping evaluate-and-break logic dynamically (`O(N)` performance). |
| Leverage a formal `Enum` class framework for `sort_tasks` to strictly clamp approved domains of sort inputs | ✅ Applied | Created `SortAttribute(Enum)` and strictly typed the function argument, eliminating fragile hardcoded string checks. |
| Instantiate native metric iterators or caching mechanisms in `summary()` to avoid looping through database records repeatedly | ✅ Applied | Optimized `summary()` to iterate through `self.tasks` exactly one time, intelligently incrementing all necessary aggregated values simultaneously. |
| Introduce a lightweight `count_overdue()` iterator resolving directly without overhead array construction | ✅ Applied | Solved inherently alongside the `summary()` optimization loop, eliminating any array generation via an integrated local counter mapping. |
| Isolate explicit task filtering architecture out of the main database into a chained object-oriented Fluent Query Builder | ❌ Rejected | Extreme over-engineering for a lightweight task manager module. Breaks YAGNI (You Aren't Gonna Need It) principles and introduces unnecessary decoupled logic complexity. |
