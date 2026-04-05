package log_analyzer

import (
	"math"
	"strconv"
	"strings"
)

type LogEntry struct {
	IPAddress  string
	Method     string
	Endpoint   string
	StatusCode int
}

type AnalysisResult struct {
	TotalRequests  int     `json:"total_requests"`
	UniqueVisitors int     `json:"unique_visitors"`
	ErrorRate      float64 `json:"error_rate"`
}

type LogAnalyzer struct{}

func NewLogAnalyzer() *LogAnalyzer {
	return &LogAnalyzer{}
}

func (a *LogAnalyzer) ParseLine(line string) *LogEntry {
	parts := strings.Fields(line)
	if len(parts) == 5 && parts[1] == "-" {
		statusCode, err := strconv.Atoi(parts[4])
		if err == nil {
			return &LogEntry{
				IPAddress:  parts[0],
				Method:     parts[2],
				Endpoint:   parts[3],
				StatusCode: statusCode,
			}
		}
	}
	return nil
}

func (a *LogAnalyzer) Analyze(lines []string) AnalysisResult {
	totalRequests := 0
	uniqueVisitorsSet := make(map[string]struct{})
	errors := 0

	for _, line := range lines {
		parsed := a.ParseLine(line)
		if parsed != nil {
			totalRequests++
			uniqueVisitorsSet[parsed.IPAddress] = struct{}{}
			if parsed.StatusCode >= 400 {
				errors++
			}
		}
	}

	errorRate := 0.0
	if totalRequests > 0 {
		errorRate = float64(errors) / float64(totalRequests)
		errorRate = math.Round(errorRate*100) / 100
	}

	return AnalysisResult{
		TotalRequests:  totalRequests,
		UniqueVisitors: len(uniqueVisitorsSet),
		ErrorRate:      errorRate,
	}
}
