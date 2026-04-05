import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer09(unittest.TestCase):
    def test_two_entries_different_visitors_both_fail(self):
        logs = ["1.1.1.1 - GET / 500", "2.2.2.2 - GET / 500"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00})
        print("✅ test_two_entries_different_visitors_both_fail: PASS", file=sys.stdout)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
