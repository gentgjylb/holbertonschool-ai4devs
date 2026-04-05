import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer07(unittest.TestCase):
    def test_single_failed_request(self):
        logs = ["8.8.8.8 - GET /api/data 503"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})

if __name__ == '__main__':
    unittest.main()
