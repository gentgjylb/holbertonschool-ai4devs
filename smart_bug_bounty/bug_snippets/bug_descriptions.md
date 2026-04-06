# Bug Descriptions

This document provides detailed descriptions for the buggy code snippets in the `bug_snippets/` directory. Each entry follows a uniform structure to ensure clarity and consistency.

---

## bug1.py
- **Language**: Python
- **Intended Behavior**:
    - **Goal**: Return the last `n` items from a list.
    - **Input**: A list `[1, 2, 3, 4, 5]` and `n = 2`.
    - **Expected Output**: `[4, 5]`.
- **Current Issue**: An off-by-one error in the slicing logic (`len(items) - n - 1`) causes the function to include one extra element at the start of the slice.
- **Bug Category**: Off-by-one Error
- **How to Fix**: Change the start index calculation on line 16 to `len(items) - n`.

---

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**:
    - **Goal**: Remove duplicate numbers from an array and return them sorted in ascending order.
    - **Input**: `[3, 1, 2, 3, 2, 4, 1]`.
    - **Expected Output**: `[1, 2, 3, 4]`.
- **Current Issue**: The logical condition is inverted; it checks if the result *already* includes the number before adding it, meaning only duplicates are (theoretically) added, but since the first instance is never added, the result stays empty.
- **Bug Category**: Logic Error (Inverted Condition)
- **How to Fix**: Negate the condition on line 9 to `!result.includes(numbers[i])`.

---

## bug3.java
- **Language**: Java
- **Intended Behavior**:
    - **Goal**: Calculate the average character length of non-null strings in a list, ignoring null entries.
    - **Input**: `Arrays.asList("hi", null, "world")`.
    - **Expected Output**: `3.5` (average of "hi" and "world").
- **Current Issue**: The code lacks a null check for elements in the list. Calling `str.length()` on a null reference triggers a `NullPointerException`.
- **Bug Category**: Runtime Exception (NullPointerException)
- **How to Fix**: Add a null check (`if (str == null) continue;`) at the beginning of the loop.

---

## bug4.py
- **Language**: Python
- **Intended Behavior**:
    - **Goal**: Sum numeric values stored as strings in a dictionary and return the total as an integer.
    - **Input**: `{"apples": "10", "oranges": "5", "pears": "2"}`.
    - **Expected Output**: `17`.
- **Current Issue**: The accumulator `total` is initialized as a string (`""`), causing the `+=` operator to perform string concatenation instead of numeric addition.
- **Bug Category**: Data Type Misuse
- **How to Fix**: Initialize `total = 0` and convert values using `int(value)` before adding.

---

## bug5.js
- **Language**: JavaScript
- **Intended Behavior**:
    - **Goal**: Fetch user data from an API and return the user's name property in uppercase.
    - **Input**: A valid `userId` (e.g., `42`).
    - **Expected Output**: A resolved promise with a string (e.g., `"ALICE"`).
- **Current Issue**: The `await` keyword is used inside a regular function. In JavaScript, `await` can only be used within an `async` function, resulting in a syntax error.
- **Bug Category**: Syntax Error
- **How to Fix**: Add the `async` keyword to the function declaration on line 4.

---

## bug6.cpp
- **Language**: C++
- **Intended Behavior**:
    - **Goal**: Reverse an array of integers in place.
    - **Input**: `int arr[] = {1, 2, 3, 4, 5}` with `size = 5`.
    - **Expected Output**: `{5, 4, 3, 2, 1}`.
- **Current Issue**: The `right` index is initialized to `size` instead of `size - 1`. This causes an out-of-bounds memory access (`arr[5]`) during the first swap.
- **Bug Category**: Memory Access Error (Out-of-Bounds)
- **How to Fix**: Initialize `right` to `size - 1` on line 9.
