# Cross-Language Specification - Log Analyzer

## Algorithm Description
Parse web server access logs to calculate key traffic statistics. The algorithm processes each entry in the log to extract the IP address, endpoint, and HTTP status code, to compute:
- **Total requests**: The sum of all valid log entries.
- **Unique visitors**: The count of distinct IP addresses.
- **Error rate**: The percentage of requests that returned an error (HTTP status codes >= 400).

## Input Format
- A list of log entry strings or a plaintext file where each line is a log entry.
- Expected Format: `[IP_ADDRESS] - [HTTP_METHOD] [ENDPOINT] [STATUS_CODE]`
- Example: `192.168.1.15 - GET /index.html 200`

## Output Format
- A JSON object (or native dictionary/map) with the statistical breakdown.
- Example:
  ```json
  {
    "total_requests": 120,
    "unique_visitors": 35,
    "error_rate": 0.05
  }
  ```

## Edge Cases
1. **Empty File / Empty List**: Handled gracefully without division by zero, returning `0` defaults.
2. **Malformed Entries**: Incomplete lines, missing delimiters, or non-numeric status codes should be skipped.
3. **Repeated Requests**: Identical IPs spamming requests should still only increment the unique visitor count exactly once.
4. **All Errors**: If all valid logs are 4xx/5xx codes, the error rate must be `1.0`.

## Test Cases

- **Test Case 1: Standard Logs with Mixed Outcomes**
  - **Input**: 
    `["192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"]`
  - **Expected Output**: 
    `{"total_requests": 4, "unique_visitors": 3, "error_rate": 0.50}`

- **Test Case 2: Empty Request Logs**
  - **Input**: `[]`
  - **Expected Output**: 
    `{"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00}`

- **Test Case 3: Dataset with 100% Error Rate**
  - **Input**: 
    `["192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"]`
  - **Expected Output**: 
    `{"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00}`

- **Test Case 4: Dataset with Malformed Entries**
  - **Input**: 
    `["192.168.1.1 - GET /home 200", "This log line is malformed", "10.0.0.5 - POST /login BAD_CODE"]`
  - **Expected Output**: 
    `{"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00}` *(Invalid lines skipped)*

- **Test Case 5: High Traffic from a Single IP**
  - **Input**: 
    `["10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"]`
  - **Expected Output**: 
    `{"total_requests": 3, "unique_visitors": 1, "error_rate": 0.33}`
