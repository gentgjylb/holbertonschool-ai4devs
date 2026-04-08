# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return exactly the last `n` items from a processed list using Python slicing.
- **Current Issue**: Off-by-one/slicing error when `n` is `0`. `processed_list[-0:]` is interpreted as `processed_list[0:]`, which returns the entire list instead of an empty list as intended. 

## bug2.js
- **Intended Behavior**: Generate an array of handler functions, where each handler returns a specific configuration string passed in an array.
- **Current Issue**: Loop variable closure bug caused by using `var`. The `for` loop binds `configName` to the function scope instead of block scope. By the time the closures are executed, they all capture the final value of `configName` (the last element).

## bug3.java
- **Intended Behavior**: Compare a list of provided string tokens against a master admin string to validate credentials.
- **Current Issue**: Uses the `==` operator for string comparison instead of `.equals()`. The `==` operator checks reference equality of strings rather than content equality, causing valid but distinct string objects (like newly trimmed strings) to incorrectly fail validation.

## bug4.py
- **Intended Behavior**: Iterate through a dictionary representing users, validate records, and remove invalid entries.
- **Current Issue**: Raises `RuntimeError: dictionary changed size during iteration`. Python does not allow modifying a dictionary's keys while iterating directly over it using `.items()`.
