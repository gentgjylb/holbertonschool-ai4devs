import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../implementations/python')))
from log_analyzer import LogAnalyzer

class TestLogAnalyzerFunctionalEquivalence(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_standard_logs(self):
        res = self.analyzer.analyze(["192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"])
        self.assertEqual(res, {"total_requests": 4, "unique_visitors": 3, "error_rate": 0.50})

    def test_empty_logs(self):
        res = self.analyzer.analyze([])
        self.assertEqual(res, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0})

    def test_100_error_rate(self):
        res = self.analyzer.analyze(["192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"])
        self.assertEqual(res, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.0})

    def test_malformed_logs(self):
        res = self.analyzer.analyze(["192.168.1.1 - GET /home 200", "Malformed line", "10.0.0.5 - POST /login BAD"])
        self.assertEqual(res, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.0})

    def test_high_traffic(self):
        res = self.analyzer.analyze(["10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"])
        self.assertEqual(res, {"total_requests": 3, "unique_visitors": 1, "error_rate": 0.33})

if __name__ == '__main__':
    unittest.main(verbosity=2)
