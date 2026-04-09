# Bug Reports

## bug1.py
- **File**: bug1.py
- **Summary**: Off-by-one/slicing error returning entire list when requesting 0 items
- **Root Cause**: The slice `processed_list[-n:]` is used to get the last `n` items. When `n` is `0`, `-0` is evaluated as `0`. The slice becomes `processed_list[0:]`, which returns the entire list rather than an empty list.
- **Resolution**: Modified the return statement to explicitly handle the `0` edge case using conditional logic (e.g., `return processed_list[-n:] if n > 0 else []`).
- **Lessons Learned**: Avoid relying on negative indexing in Python without checking for zero, as negative zero evaluates to zero and changes the slice starting point unexpectedly.
- **Expected Outcome**: The function correctly returns an empty list when 0 items are requested, and the correct number of last items otherwise. All 3 test cases passed.

## bug2.js
- **File**: bug2.js
- **Summary**: Loop variable closure bug caused by using `var`
- **Root Cause**: The loop relies on the `var` keyword to declare the loop variable. `var` is function-scoped rather than block-scoped, meaning every closure generated in the loop captures the exact same variable reference, resulting in all handlers returning the last item's value.
- **Resolution**: Replaced `var` with `let` when declaring loop variables to provide block scoping. This ensures each iteration securely binds its own snapshot of the variable for the closures.
- **Lessons Learned**: Always use `let` or `const` instead of `var` in JavaScript to declare variables within loops when creating closures, ensuring proper block scoping.
- **Expected Outcome**: Each generated handler uniquely preserves its configuration string and correctly returns it when called. All 3 test cases passed.

## bug3.java
- **File**: bug3.java
- **Summary**: Incorrect string comparison logic using the `==` operator
- **Root Cause**: The logic uses the `==` operator to compare a dynamically created string (from `.trim()`) against a master string. In Java, `==` checks for strict mathematical/memory reference equality instead of character content equality.
- **Resolution**: Altered the condition to utilize the `.equals()` method, which precisely isolates and evaluates the character content of the objects rather than their memory allocations.
- **Lessons Learned**: Never use `==` for String comparison in Java; always use the `.equals()` method to verify content equality.
- **Expected Outcome**: Valid string tokens accurately match the master admin string and authenticate properly. All 3 test cases passed.

## bug4.py
- **File**: bug4.py
- **Summary**: `RuntimeError` due to dictionary changing size during iteration
- **Root Cause**: The code attempts to delete keys from the dictionary while currently actively iterating over it using `.items()`. Python explicitly forbids mutating a dictionary's size while modifying an active iterator view.
- **Resolution**: Traversed a fully static snapshot generated via `list(user_database.items())`, resolving the conflict and allowing unpenalized live database edits inside the loop.
- **Lessons Learned**: Never directly mutate a collection (like deleting dictionary keys) while actively iterating over its live elements. Always iterate over a static copy or snapshot instead.
- **Expected Outcome**: Invalid records are dynamically removed from the active dictionary without triggering runtime iteration exceptions. All 3 test cases passed.
