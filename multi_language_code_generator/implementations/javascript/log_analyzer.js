class LogAnalyzer {
    parseLine(line) {
        // Splits by arbitrary whitespace
        const parts = line.trim().split(/\s+/);
        
        if (parts.length === 5 && parts[1] === '-') {
            const statusCode = parseInt(parts[4], 10);
            if (!isNaN(statusCode)) {
                return {
                    ip_address: parts[0],
                    method: parts[2],
                    endpoint: parts[3],
                    status_code: statusCode
                };
            }
        }
        return null;
    }

    analyze(lines) {
        let total_requests = 0;
        const unique_visitors_set = new Set();
        let errors = 0;

        for (const line of lines) {
            const parsed = this.parseLine(line);
            if (parsed !== null) {
                total_requests += 1;
                unique_visitors_set.add(parsed.ip_address);
                if (parsed.status_code >= 400) {
                    errors += 1;
                }
            }
        }

        let error_rate = 0.0;
        if (total_requests > 0) {
            error_rate = Math.round((errors / total_requests) * 100) / 100;
        }

        return {
            total_requests: total_requests,
            unique_visitors: unique_visitors_set.size,
            error_rate: error_rate
        };
    }
}

module.exports = LogAnalyzer;
