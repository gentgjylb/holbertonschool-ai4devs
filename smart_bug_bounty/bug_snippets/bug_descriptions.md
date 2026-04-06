# Bug Descriptions

## bug1.py
- **Language**: Python
- **Intended Behavior**: Return the last `n` items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing. `start` is computed as `len(items) - n - 1` instead of `len(items) - n`, so the function returns `n + 1` items instead of `n`.
- **Example**: `last_n([1, 2, 3, 4, 5], 2)` should return `[4, 5]` but returns `[3, 4, 5]`.

---

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**: Remove duplicate numbers from an array and return a sorted list of unique values in ascending order.
- **Current Issue**: Logical error — the condition `result.includes(numbers[i])` is inverted. The function only pushes a number when it already exists in `result`, so nothing ever gets added and the output is always an empty array `[]`.
- **Example**: `dedupeAndSort([3, 1, 2, 3, 2, 4, 1])` should return `[1, 2, 3, 4]` but returns `[]`.

---

## bug3.java
- **Language**: Java
- **Intended Behavior**: Calculate the average character length of non-null strings in a list, silently ignoring any `null` entries.
- **Current Issue**: No null check before calling `str.length()`. When the list contains `null` values, the program throws a `NullPointerException` at runtime instead of gracefully skipping those entries.
- **Example**: `averageLength(Arrays.asList("hi", null, "world"))` should return `3.5` but throws `NullPointerException`.

---

## bug4.py
- **Language**: Python
- **Intended Behavior**: Sum all values in a dictionary where values are numbers stored as strings, and return the total as an integer.
- **Current Issue**: Data type misuse — `total` is initialized as an empty string `""` instead of `0`, so `+=` performs string concatenation rather than numeric addition.
- **Example**: `sum_string_values({"apples": "10", "oranges": "5", "pears": "2"})` should return `17` but returns `"1052"`.

---

## bug5.js
- **Language**: JavaScript
- **Intended Behavior**: Asynchronously fetch user data from an API endpoint and return the user's `name` field converted to uppercase. The function should return a `Promise<string>` so callers can `await` the result.
- **Current Issue**: Syntax error — `await` is used inside a regular (non-`async`) function. This causes a `SyntaxError` at parse time, preventing the script from running at all. The function declaration is missing the `async` keyword.
- **Example**: `fetchUserNameUpper(42)` should resolve to `"ALICE"` but throws `SyntaxError: await is only valid in async functions`.

---

## bug6.go
- **Language**: Go
- **Intended Behavior**: Compute the factorial of a non-negative integer `n` and return the result.
- **Current Issue**: Integer overflow — the accumulator `result` is declared as `int32`, which has a maximum value of `2,147,483,647`. Factorials grow rapidly: `13! = 6,227,020,800`, which exceeds `int32` range, causing the result to silently wrap around to a wrong (negative) value. The function should use `int64` or `*big.Int` to handle larger inputs correctly.
- **Example**: `factorial(13)` should return `6227020800` but returns `-2147483648` (overflow).
