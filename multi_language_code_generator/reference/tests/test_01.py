import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer01(unittest.TestCase):
    def test_empty_request_logs(self):
        logs = []
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})

if __name__ == '__main__':
    unittest.main()
