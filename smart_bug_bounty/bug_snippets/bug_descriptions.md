# Bug Descriptions

This document describes the intended behavior and current issues for each buggy code snippet in the `bug_snippets/` directory. There are 6 snippets across 4 languages (Python, JavaScript, Java, C++).

---

## bug1.py
- **Language**: Python
- **Intended Behavior**: The function `last_n(items, n)` should return the last `n` items from a given list. For example, `last_n([1, 2, 3, 4, 5], 2)` should return `[4, 5]`.
- **Current Issue**: Off-by-one error in the slice start index. The start index is calculated as `len(items) - n - 1` instead of `len(items) - n`. This causes the function to return `n + 1` items instead of `n` items. For the example above, it incorrectly returns `[3, 4, 5]`.
- **Bug Category**: Off-by-one error
- **How to Fix**: Change `len(items) - n - 1` to `len(items) - n` on line 16.

---

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**: The function `dedupeAndSort(numbers)` should remove duplicate values from an array of numbers and return the unique values sorted in ascending order. For example, `dedupeAndSort([3, 1, 2, 3, 2, 4, 1])` should return `[1, 2, 3, 4]`.
- **Current Issue**: The conditional logic for detecting duplicates is inverted. The `if (result.includes(numbers[i]))` check pushes a number into the result only when it is *already* present — meaning the first occurrence of any value is always skipped, and only subsequent duplicates get added. Since unique numbers are never added, the function always returns an empty array `[]`.
- **Bug Category**: Logic error (inverted condition)
- **How to Fix**: Negate the condition to `if (!result.includes(numbers[i]))` on line 9 so that a number is added only when it is *not* already in the result.

---

## bug3.java
- **Language**: Java
- **Intended Behavior**: The method `averageLength(List<String> items)` should calculate the average character length of all non-null strings in the provided list, silently ignoring any `null` entries. For example, `averageLength(["hi", null, "world"])` should return `3.5` (average of lengths 2 and 5), not include `null` in the count.
- **Current Issue**: There is no null check before calling `str.length()` in the for-each loop. When the list contains `null` entries, the program throws a `NullPointerException` at runtime instead of skipping them as intended.
- **Bug Category**: Missing null guard / runtime exception
- **How to Fix**: Add a `if (str == null) continue;` check at the start of the loop body (before line 14) to skip null entries.

---

## bug4.py
- **Language**: Python
- **Intended Behavior**: The function `sum_string_values(values)` should take a dictionary whose values are numbers stored as strings (e.g., `{"apples": "10", "oranges": "5"}`) and return their integer sum. For the example, the expected return value is `17`.
- **Current Issue**: The accumulator `total` is initialized as an empty string `""` instead of the integer `0`. As a result, the `+=` operator performs string concatenation (producing `"1052"`) rather than numeric addition. Additionally, individual values are never converted to integers with `int()`.
- **Bug Category**: Data type misuse (string vs. integer)
- **How to Fix**: Initialize `total = 0` on line 11, and convert each value to an integer before adding: `total += int(value)` on line 14.

---

## bug5.js
- **Language**: JavaScript
- **Intended Behavior**: The function `fetchUserNameUpper(userId)` should make an HTTP request to an API endpoint, retrieve the JSON response containing user data, and return the user's name converted to uppercase. For example, for a user named "Alice", the function should resolve to `"ALICE"`.
- **Current Issue**: The function uses the `await` keyword inside a regular (non-async) function declaration. In JavaScript, `await` is only valid inside functions declared with the `async` keyword. This causes a `SyntaxError` at parse time, preventing the code from running at all.
- **Bug Category**: Syntax error (missing `async` keyword)
- **How to Fix**: Add the `async` keyword to the function declaration on line 4: `async function fetchUserNameUpper(userId)`.

---

## bug6.cpp
- **Language**: C++
- **Intended Behavior**: The function `reverseArray(int arr[], int size)` should reverse an array of integers in place using the two-pointer swap technique. For example, given `{1, 2, 3, 4, 5}`, the array should become `{5, 4, 3, 2, 1}` after the function call.
- **Current Issue**: The `right` pointer is initialized to `size` instead of `size - 1`. Since valid array indices range from `0` to `size - 1`, the first swap accesses `arr[size]`, which is out of bounds. In C++, this leads to undefined behavior — potentially corrupting adjacent memory, producing wrong results, or crashing.
- **Bug Category**: Array index out of bounds
- **How to Fix**: Change `int right = size;` to `int right = size - 1;` on line 9.
