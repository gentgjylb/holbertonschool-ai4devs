import os

test_dir = r"c:\Users\Gent\holbertonschool-ai4devs\multi_language_code_generator\reference\tests"
os.makedirs(test_dir, exist_ok=True)

tests = [
    (
        "test_00.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer00(unittest.TestCase):\n    def test_standard_logs_mixed_outcomes(self):\n        logs = ["192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 4, "unique_visitors": 3, "error_rate": 0.50})"""
    ),
    (
        "test_01.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer01(unittest.TestCase):\n    def test_empty_request_logs(self):\n        logs = []\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})"""
    ),
    (
        "test_02.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer02(unittest.TestCase):\n    def test_dataset_100_percent_error_rate(self):\n        logs = ["192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00})"""
    ),
    (
        "test_03.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer03(unittest.TestCase):\n    def test_dataset_with_malformed_entries(self):\n        logs = ["192.168.1.1 - GET /home 200", "This log line is malformed", "10.0.0.5 - POST /login BAD_CODE"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})"""
    ),
    (
        "test_04.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer04(unittest.TestCase):\n    def test_high_traffic_single_ip(self):\n        logs = ["10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 3, "unique_visitors": 1, "error_rate": 0.33})"""
    ),
    (
        "test_05.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer05(unittest.TestCase):\n    def test_all_malformed_entries(self):\n        logs = ["completely invalid log entry", "192.168.1.1 GET /dashboard 200", "192.168.1.2 - /home 200"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.00})"""
    ),
    (
        "test_06.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer06(unittest.TestCase):\n    def test_single_successful_request(self):\n        logs = ["8.8.8.8 - OPTIONS /api/status 204"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.00})"""
    ),
    (
        "test_07.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer07(unittest.TestCase):\n    def test_single_failed_request(self):\n        logs = ["8.8.8.8 - GET /api/data 503"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})"""
    ),
    (
        "test_08.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer08(unittest.TestCase):\n    def test_arbitrary_whitespace(self):\n        logs = ["10.0.0.1      -    GET    /path     500"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 1, "unique_visitors": 1, "error_rate": 1.00})"""
    ),
    (
        "test_09.py",
        """import sys\nimport os\nimport unittest\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\nfrom log_analyzer import LogAnalyzer\nclass TestLogAnalyzer09(unittest.TestCase):\n    def test_two_entries_different_visitors_both_fail(self):\n        logs = ["1.1.1.1 - GET / 500", "2.2.2.2 - GET / 500"]\n        result = LogAnalyzer().analyze(logs)\n        self.assertEqual(result, {"total_requests": 2, "unique_visitors": 2, "error_rate": 1.00})"""
    )
]

for filename, content in tests:
    with open(os.path.join(test_dir, filename), "w") as f:
        f.write(content + "\nif __name__ == '__main__':\n    unittest.main()\n")
