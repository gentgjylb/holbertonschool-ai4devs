import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer04(unittest.TestCase):
    def test_high_traffic_single_ip(self):
        logs = ["10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 3, "unique_visitors": 1, "error_rate": 0.33})

if __name__ == '__main__':
    unittest.main()
