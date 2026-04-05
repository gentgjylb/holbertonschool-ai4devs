const assert = require('assert');
const path = require('path');
const LogAnalyzer = require('../../implementations/javascript/log_analyzer.js');

function runFunctionalEquivalenceTests() {
    const analyzer = new LogAnalyzer();

    // Test 1: Standard Logs
    const res1 = analyzer.analyze(["192.168.1.1 - GET /home 200", "10.0.0.5 - POST /login 401", "192.168.1.1 - GET /dashboard 200", "172.16.0.4 - GET /logo.png 404"]);
    assert.deepStrictEqual(res1, {total_requests: 4, unique_visitors: 3, error_rate: 0.50});

    // Test 2: Empty Logs
    const res2 = analyzer.analyze([]);
    assert.deepStrictEqual(res2, {total_requests: 0, unique_visitors: 0, error_rate: 0.0});

    // Test 3: 100% Error Rate
    const res3 = analyzer.analyze(["192.168.0.1 - GET /api/data 500", "192.168.0.2 - GET /api/data 403"]);
    assert.deepStrictEqual(res3, {total_requests: 2, unique_visitors: 2, error_rate: 1.0});

    // Test 4: Malformed Logs Skipped
    const res4 = analyzer.analyze(["192.168.1.1 - GET /home 200", "Malformed line", "10.0.0.5 - POST /login BAD"]);
    assert.deepStrictEqual(res4, {total_requests: 1, unique_visitors: 1, error_rate: 0.0});

    // Test 5: High Traffic
    const res5 = analyzer.analyze(["10.1.1.1 - GET /page1 200", "10.1.1.1 - GET /page2 200", "10.1.1.1 - GET /page3 400"]);
    assert.deepStrictEqual(res5, {total_requests: 3, unique_visitors: 1, error_rate: 0.33});

    console.log("✅ JavaScript Functional Equivalence Tests Passed Successfully.");
}

runFunctionalEquivalenceTests();
