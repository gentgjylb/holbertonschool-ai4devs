## Section 1 - PaymentProcessor::validate()

- **Plain English**: Validates credit card number and expiry.
- **Pattern**: Uses nested if-else instead of guard clauses.
- **Issues**: No logging, weak validation.
- **Improvements**: Replace with regex validation + unit tests.

## Section 2 - OrderService::processTransaction()

- **Plain English**: Handles the checkout process, deducting inventory and finalizing the transaction.
- **Pattern**: God object pattern with a massive monolithic method managing multiple responsibilities.
- **Issues**: Deeply nested database calls inside loops, prone to race conditions.
- **Improvements**: Refactor into smaller domain services and implement database transactions.

## Section 3 - UserAuthentication::verifyLogin()

- **Plain English**: Checks user credentials against the database and establishes a session.
- **Pattern**: Direct hardcoded SQL queries inline with business logic.
- **Issues**: Vulnerable to SQL injection attacks, relies on outdated MD5 hashing.
- **Improvements**: Transition to Prepared Statements and migrate to secure bcrypt hashing.

## Section 4 - CartManager::calculateDiscount()

- **Plain English**: Determines the applicable discount codes based on cart contents and promotional rules.
- **Pattern**: Hardcoded magic numbers and complex switch/case statements.
- **Issues**: Adding new discount rules requires modifying core business logic directly.
- **Improvements**: Implement the Strategy design pattern and move rules to a database table.

## Section 5 - ReportGenerator::exportSalesToExcel()

- **Plain English**: Queries the reporting database and formats the results into a downloadable CSV stream.
- **Pattern**: Loads the entire dataset into memory before processing.
- **Issues**: High memory consumption causing OutOfMemoryErrors for large date ranges.
- **Improvements**: Implement database cursor streaming and write to the output stream in batches.
