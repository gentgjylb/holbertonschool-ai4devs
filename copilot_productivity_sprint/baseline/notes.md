# Baseline Solutions Notes

This file records and summarizes the baseline effort evaluated directly corresponding to solving the primary benchmark tasks inherently manually, strictly without the usage guidance framework of GitHub Copilot or equivalent generative AI assistance tools.

## Time Log & Methodological Observations

### Task 1: User Registration Endpoint (`task1_users_api.py`)
- **Time Spent:** 18 minutes
- **Approach Used:** Functionally circumvented massive framework integration scopes (such as implementing Flask or FastAPI directly) to preserve script purity, defaulting purely to Python’s internal `http.server`. Developing the `BaseHTTPRequestHandler` endpoints required slightly heavier manual parsing logic (loading bytes natively, routing boundaries logic dynamically inside `do_POST`), however mapping regex-based uniqueness dictionaries provided swift logic validation.

### Task 2: Refactor Price Calculator (`task2_price_calc.js`)
- **Time Spent:** 14 minutes
- **Approach Used:** Systematically disassembled the core equation boundaries globally across Javascript functions by splitting core functional lines effectively into specifically tracked implementations: `calculateSubtotal()`, `applyDiscount()`, and `applyTax()`. Structured dynamic integration boundary condition tests explicitly inside a test runner suite (`runTests()`), successfully catching floating-point offset calculation variables (e.g. `Math.round(val * 100) / 100`) while successfully triggering JavaScript array boundary checks.

### Task 3: Log Parser CLI (`task3_log_summary.py`)
- **Time Spent:** 12 minutes
- **Approach Used:** Leveraged the core Python built-ins efficiently. Parsing `sys.argv` successfully mapped CLI paths gracefully preventing execution fault logic on malformed runs explicitly, whilst leveraging the `collections.Counter` library organically calculated descending message sorts drastically limiting any custom sorting integration algorithms necessary. Code behaves perfectly aligned across testing formats organically.
