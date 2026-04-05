package log_analyzer_test

import (
	"reflect"
	"testing"
    
	// Assuming module path is standard or can be adjusted based on go module init
	la "multi_language_code_generator/implementations/go"
)

func TestLogAnalyzerFunctionalEquivalence(t *testing.T) {
	analyzer := la.NewLogAnalyzer()

	// Test 1: Standard Logs
	res1 := analyzer.Analyze([]string{"192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"})
	exp1 := la.AnalysisResult{TotalRequests: 4, UniqueVisitors: 3, ErrorRate: 0.50}
	if !reflect.DeepEqual(res1, exp1) {
		t.Errorf("TC1 Failed: expected %v, got %v", exp1, res1)
	}

	// Test 2: Empty Logs
	res2 := analyzer.Analyze([]string{})
	exp2 := la.AnalysisResult{TotalRequests: 0, UniqueVisitors: 0, ErrorRate: 0.0}
	if !reflect.DeepEqual(res2, exp2) {
		t.Errorf("TC2 Failed: expected %v, got %v", exp2, res2)
	}

	// Test 3: 100 Error Rate
	res3 := analyzer.Analyze([]string{"192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"})
	exp3 := la.AnalysisResult{TotalRequests: 2, UniqueVisitors: 2, ErrorRate: 1.0}
	if !reflect.DeepEqual(res3, exp3) {
		t.Errorf("TC3 Failed: expected %v, got %v", exp3, res3)
	}

	// Test 4: Malformed Logs Skipped
	res4 := analyzer.Analyze([]string{"192.168.1.1 - GET /home 200", "Malformed line", "10.0.0.5 - POST /login BAD"})
	exp4 := la.AnalysisResult{TotalRequests: 1, UniqueVisitors: 1, ErrorRate: 0.0}
	if !reflect.DeepEqual(res4, exp4) {
		t.Errorf("TC4 Failed: expected %v, got %v", exp4, res4)
	}

	// Test 5: High Traffic
	res5 := analyzer.Analyze([]string{"10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"})
	exp5 := la.AnalysisResult{TotalRequests: 3, UniqueVisitors: 1, ErrorRate: 0.33}
	if !reflect.DeepEqual(res5, exp5) {
		t.Errorf("TC5 Failed: expected %v, got %v", exp5, res5)
	}
}
