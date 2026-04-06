# Bug Descriptions

## bug1.py
- **Language**: Python
- **Intended Behavior**: Process a list of sales transaction records, aggregate total sales per salesperson by accumulating all their individual amounts, and return exactly the top `N` salespeople sorted by descending total sales.
- **Current Issue (Bug 1 — wrong assignment operator)**: Inside `process_data()`, the line `self.sales_by_person[name] = amount` uses `=` instead of `+=`. This means every new transaction for the same person overwrites the previous total instead of adding to it. Only the last transaction amount is kept.
- **Current Issue (Bug 2 — off-by-one in slice)**: Inside `get_top_n_salespeople()`, the slice `sorted_sales[0:n+1]` returns `n+1` results instead of the requested `n`, causing one extra salesperson to always appear in the output.

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**: Manage a shopping cart by adding items (name, price, quantity), optionally applying a promo discount code, and calculating the correct subtotal, discount amount, and final total — all formatted to two decimal places.
- **Current Issue**: In `calculateTotal()`, the loop uses `for (let item in this.items)`. In JavaScript, `for...in` on an array iterates over the **index keys** (the strings `"0"`, `"1"`, etc.), not the element objects. Consequently `item.price` and `item.quantity` are both `undefined`, and every multiplication yields `NaN`, producing an entirely incorrect total.

## bug3.java
- **Language**: Java
- **Intended Behavior**: Maintain a list of enrolled students, allow removing a student by name, and compute the current average GPA of all remaining students.
- **Current Issue**: In `removeStudent()`, the code calls `students.remove(s)` while actively iterating over `students` with a for-each loop. Java's `ArrayList` iterator detects structural modification during iteration and immediately throws a `ConcurrentModificationException`. The fix is to use `Iterator.remove()` or `students.removeIf(s -> s.getName().equals(name))`.

## bug4.py
- **Language**: Python
- **Intended Behavior**: A `ConfigManager` that holds immutable factory defaults, allows user overrides to be layered on top at runtime, and can reset the active configuration back to the original defaults at any time.
- **Current Issue**: In `__init__()`, `self.current_config = self.default_config` does **not** copy the dictionary — both attributes point to the exact same object in memory. Any mutation to `self.current_config` (including list `.extend()` calls) silently mutates `self.default_config` as well. When `reset_config()` reassigns `self.current_config = self.default_config`, the "defaults" object is already corrupted, so the reset has no effect.

## bug5.js
- **Language**: JavaScript
- **Intended Behavior**: Schedule named callbacks to run after a specified delay. Upon execution each callback should be removed from the pending-tasks list and the completed-tasks counter should be incremented, so `getStatus()` always returns accurate pending/completed counts.
- **Current Issue**: The `setTimeout` callback is a regular `function` expression, which does **not** inherit `this` from the enclosing `TaskScheduler` instance. At the time the callback fires, `this` is `undefined` (strict mode) or the global object, making `this.tasks.indexOf(taskName)` throw a `TypeError`. Fix by using an arrow function `() => { … }` or by capturing the context with `.bind(this)`.

## bug6.go
- **Language**: Go
- **Intended Behavior**: A `BankAccount` struct that safely receives many concurrent deposits from multiple goroutines and ends with a balance that is exactly `numDeposits × depositAmount`.
- **Current Issue**: `BankAccount` has no `sync.Mutex` (or other synchronization primitive). The `Deposit` method performs a non-atomic read-modify-write on `a.balance` (`a.balance += amount`). When thousands of goroutines execute this simultaneously, multiple goroutines read the same stale value, increment it, and write back — overwriting each other's work. The final balance is unpredictable and almost always less than expected (detectable with `go run -race`).
