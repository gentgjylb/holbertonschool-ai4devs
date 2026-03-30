## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items from a list.
**Issue Type**: Syntax error.
**Notes**: The function definition is missing a colon after `def get_last_items(items, n)`, so the code cannot be parsed.

## Bug 2 – bug2.js
**Intended Behavior**: Filter a score list to return only odd scores.
**Issue Type**: Logical error.
**Notes**: The condition uses `score % 2 === 0`, so the function returns even scores instead of odd ones.

## Bug 3 – bug3.java
**Intended Behavior**: Convert and print a username for a valid user ID.
**Issue Type**: Runtime exception.
**Notes**: When `userId` is not "admin", `user` stays `null`, and `user.toUpperCase()` throws a `NullPointerException`.

## Bug 4 – bug4.cpp
**Intended Behavior**: Sum all values in a vector.
**Issue Type**: Off-by-one / loop logic issue.
**Notes**: The loop condition uses `i <= values.size()`, causing an out-of-range access on the final iteration.

## Bug 5 – bug5.py
**Intended Behavior**: Save a user profile to JSON and then load it back.
**Issue Type**: Misuse of data types / libraries.
**Notes**: `load_profile` calls `json.loads` on a dictionary instead of a JSON string, causing a `TypeError`.
