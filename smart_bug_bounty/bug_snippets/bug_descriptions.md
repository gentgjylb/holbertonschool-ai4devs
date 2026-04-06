# Bug Descriptions

## bug1.py
- **Intended Behavior**: Process a list of sales transactions, aggregate total sales per salesperson by accumulating all their amounts, and return exactly the top N salespeople sorted by descending total.
- **Current Issue**: Two bugs are present. First, `self.sales_by_person[name] = amount` uses `=` instead of `+=`, overwriting previous sales instead of accumulating them. Second, the slice `sorted_sales[0:n+1]` has an off-by-one error that returns `n+1` results instead of `n`.

## bug2.js
- **Intended Behavior**: Manage a shopping cart by adding items with a name, price, and quantity, optionally applying a promo discount code, then computing the correct subtotal, discount amount, and final total.
- **Current Issue**: `calculateTotal()` uses `for (let item in this.items)` which iterates over array index strings (`"0"`, `"1"`, …) instead of the item objects. Both `item.price` and `item.quantity` are `undefined`, so every multiplication yields `NaN` and the total is incorrect.

## bug3.java
- **Intended Behavior**: Maintain a list of enrolled students, support removing a student by name, and compute the current average GPA across all remaining students.
- **Current Issue**: `removeStudent()` calls `students.remove(s)` while iterating over the same list with a for-each loop. Java's iterator detects the structural modification and throws `ConcurrentModificationException` at runtime.

## bug4.py
- **Intended Behavior**: A configuration manager that stores immutable factory defaults, allows user overrides to be merged in at runtime, and can reset the active configuration back to the original defaults at any time.
- **Current Issue**: `self.current_config = self.default_config` creates a reference alias, not a copy. Both variables point to the same dictionary object, so any mutation through `current_config` permanently corrupts `default_config` as well, making `reset_config()` ineffective.

## bug5.js
- **Intended Behavior**: Schedule named callbacks to fire after a specified delay. After each callback executes, its task should be removed from the pending list and the completed counter should be incremented so `getStatus()` always reflects accurate counts.
- **Current Issue**: The `setTimeout` callback uses a regular `function` expression which does not inherit `this` from the enclosing `TaskScheduler` instance. When the callback fires, `this` is `undefined` (strict mode) or the global object, causing `this.tasks.indexOf()` to throw a `TypeError`.

## bug6.go
- **Intended Behavior**: A `BankAccount` struct that safely accepts many concurrent deposits from multiple goroutines, finishing with a final balance equal to `numDeposits × depositAmount`.
- **Current Issue**: `BankAccount` has no `sync.Mutex`. The `Deposit` method performs a non-atomic read-modify-write on `a.balance`. When many goroutines run concurrently, they overwrite each other's updates, leading to a data race and an unpredictably low final balance (detectable with `go run -race`).
