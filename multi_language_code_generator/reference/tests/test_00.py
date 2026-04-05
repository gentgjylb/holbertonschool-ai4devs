import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer00(unittest.TestCase):
    def test_standard_logs_mixed_outcomes(self):
        logs = ["192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result, {"total_requests": 4, "unique_visitors": 3, "error_rate": 0.50})
        print("✅ test_standard_logs_mixed_outcomes: PASS", file=sys.stdout)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
