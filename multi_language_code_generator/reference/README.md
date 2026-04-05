# Reference Implementation: Log Analyzer

This directory contains the reference implementation of the Log Analyzer algorithm in Python.

## Files
- `log_analyzer.py`: Contains the `LogAnalyzer` class which parses and analyzes logs to return the overall `total_requests`, `unique_visitors`, and `error_rate`.
- `tests/`: Contains 10 separate test files ensuring complete coverage of the `LogAnalyzer` edge cases and standard usage.
- `test_results.log`: Contains the execution output verifying that all 10 tests passed successfully.

## Test Results

All 10 test cases in unit testing pass successfully without any errors. Please view `test_results.log` for the exact output of test runs.

Run the tests using:
```bash
python3 -m unittest discover tests
```
