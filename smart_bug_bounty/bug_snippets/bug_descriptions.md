# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing. The start index is computed as `len(items) - n - 1` instead of `len(items) - n`, so the function returns n+1 items instead of n.

## bug2.js
- **Intended Behavior**: Remove duplicate numbers from an array and return them sorted in ascending order.
- **Current Issue**: Logical error — the condition is inverted. The function pushes a number only when it already exists in `result`, so unique values never get added and the output is always an empty array.

## bug3.java
- **Intended Behavior**: Calculate the average character length of non-null strings in a list, ignoring null entries.
- **Current Issue**: Missing null check before calling `str.length()`. When the list contains null values, the program throws a `NullPointerException` instead of skipping them.

## bug4.py
- **Intended Behavior**: Sum all values in a dictionary where the values are numbers stored as strings, returning an integer total.
- **Current Issue**: Data type misuse — `total` is initialized as an empty string instead of `0`, so `+=` performs string concatenation rather than numeric addition.

## bug5.js
- **Intended Behavior**: Fetch user data from an API and return the user's name in uppercase.
- **Current Issue**: `await` is used inside a regular (non-async) function, causing a SyntaxError. The function declaration is missing the `async` keyword.

## bug6.go
- **Intended Behavior**: Compute the factorial of a non-negative integer and return the correct result.
- **Current Issue**: Integer overflow — the accumulator is declared as `int32`, which overflows for inputs >= 13. Should use `int64` or `big.Int`.
