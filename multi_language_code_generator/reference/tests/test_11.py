import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer11(unittest.TestCase):
    def test_missing_ip_address_but_5_parts(self):
        logs = ["- - GET /path 200"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})

if __name__ == '__main__':
    unittest.main()
