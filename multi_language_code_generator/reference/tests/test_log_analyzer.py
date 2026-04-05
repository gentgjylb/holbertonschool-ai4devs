import unittest
import sys
import os

# Add the reference directory to the path so we can import the log_analyzer module easily
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_standard_logs_mixed_outcomes(self):
        # Test Case 1 from spec
        logs = [
            "192.168.1.1 - GET /home 200", 
            "10.0.0.5 - POST /login 401", 
            "192.168.1.1 - GET /dashboard 200", 
            "172.16.0.4 - GET /logo.png 404"
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 4, "unique_visitors": 3, "error_rate": 0.50})

    def test_empty_request_logs(self):
        # Test Case 2 from spec
        logs = []
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})

    def test_dataset_100_percent_error_rate(self):
        # Test Case 3 from spec
        logs = [
            "192.168.0.1 - GET /api/data 500", 
            "192.168.0.2 - GET /api/data 403"
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00})

    def test_dataset_with_malformed_entries(self):
        # Test Case 4 from spec
        logs = [
            "192.168.1.1 - GET /home 200", 
            "This log line is malformed", 
            "10.0.0.5 - POST /login BAD_CODE"
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})

    def test_high_traffic_single_ip(self):
        # Test Case 5 from spec
        logs = [
            "10.1.1.1 - GET /page1 200", 
            "10.1.1.1 - GET /page2 200", 
            "10.1.1.1 - GET /page3 400"
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 3, "unique_visitors": 1, "error_rate": 0.33})

    def test_all_malformed_entries(self):
        # Extra Test Case 6: Completely garbage data
        logs = [
            "completely invalid log entry 1",
            "192.168.1.1 GET /dashboard 200", # Missing hyphen
            "192.168.1.2 - /home 200", # Missing HTTP Method
            "192.168.1.3 - GET 200" # Missing Endpoint
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})

    def test_single_successful_request(self):
        # Extra Test Case 7: Only one valid log entry - success
        logs = ["8.8.8.8 - OPTIONS /api/status 204"]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})

    def test_single_failed_request(self):
        # Extra Test Case 8: Only one valid log entry - failure
        logs = ["8.8.8.8 - GET /api/data 503"]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})

    def test_arbitrary_whitespace(self):
        # Extra Test Case 9: Logs with extra spacing
        logs = ["10.0.0.1      -    GET    /path     500"]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})

    def test_large_input_alternating_status(self):
        # Extra Test Case 10: 100 entries from two IPs alternating success and failure
        logs = []
        for i in range(50):
            logs.append("192.168.1.10 - GET /home 200")
            logs.append("192.168.1.11 - POST /submit 500")
        
        result = self.analyzer.analyze(logs)
        self.assertEqual(result, {"total_requests": 100, "unique_visitors": 2, "error_rate": 0.50})

if __name__ == '__main__':
    unittest.main()
