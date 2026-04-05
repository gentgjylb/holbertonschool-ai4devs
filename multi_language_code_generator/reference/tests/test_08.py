import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer08(unittest.TestCase):
    def test_arbitrary_whitespace(self):
        logs = ["10.0.0.1      -    GET    /path     500"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})
        print("✅ test_arbitrary_whitespace: PASS", file=sys.stdout)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
