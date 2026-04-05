import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer02(unittest.TestCase):
    def test_dataset_100_percent_error_rate(self):
        logs = ["192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00})
        print("✅ test_dataset_100_percent_error_rate: PASS", file=sys.stdout)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
