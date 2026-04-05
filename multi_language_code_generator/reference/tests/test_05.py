import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer05(unittest.TestCase):
    def test_all_malformed_entries(self):
        logs = ["completely invalid log entry", "192.168.1.1 GET /dashboard 200", "192.168.1.2 - /home 200"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})

if __name__ == '__main__':
    unittest.main()
