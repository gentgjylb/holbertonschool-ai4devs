class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        """
        Parses a web server log line and returns a dictionary with extracted features, 
        or None if the entry is malformed.
        Expected format: [IP_ADDRESS] - [HTTP_METHOD] [ENDPOINT] [STATUS_CODE]
        """
        parts = line.split()
        if len(parts) == 5 and parts[1] == '-':
            try:
                return {
                    "ip_address": parts[0],
                    "method": parts[2],
                    "endpoint": parts[3],
                    "status_code": int(parts[4])
                }
            except ValueError:
                # Status code was not an integer
                pass
        return None

    def analyze(self, lines: list[str]) -> dict:
        """
        Analyzes a list of log entries to compute total requests, unique visitors, and error rate.
        Skips gracefully any malformed entry.
        """
        total_requests = 0
        unique_visitors_set = set()
        errors = 0

        for line in lines:
            parsed = self.parse_line(line)
            if parsed is not None:
                total_requests += 1
                unique_visitors_set.add(parsed["ip_address"])
                if parsed["status_code"] >= 400:
                    errors += 1
        
        error_rate = 0.0
        if total_requests > 0:
            error_rate = round(errors / total_requests, 2)

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_visitors_set),
            "error_rate": error_rate
        }
