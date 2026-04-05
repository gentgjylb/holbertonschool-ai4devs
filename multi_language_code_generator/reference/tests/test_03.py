import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer03(unittest.TestCase):
    def test_dataset_with_malformed_entries(self):
        logs = ["192.168.1.1 - GET /home 200", "This log line is malformed", "10.0.0.5 - POST /login BAD_CODE"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})

if __name__ == '__main__':
    unittest.main()
