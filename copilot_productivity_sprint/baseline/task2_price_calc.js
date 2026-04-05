const assert = require('assert');

// --- Helper Functions ---

function calculateSubtotal(items) {
    if (!items || items.length === 0) return 0;
    return items.reduce((total, item) => total + (item.price * item.quantity), 0);
}

function applyDiscount(subtotal, discountCode) {
    if (discountCode === 'SAVE10') {
        const discount = subtotal * 0.10;
        return subtotal - discount;
    }
    return subtotal;
}

function applyTax(amount, taxRate) {
    return amount + (amount * taxRate);
}

// --- Main Refactored Function ---

function calculateTotal(items, taxRate, discountCode) {
    if (!items || items.length === 0) return 0;
    
    // Step-by-step distinct pipeline tracking
    const subtotal = calculateSubtotal(items);
    const discounted = applyDiscount(subtotal, discountCode);
    const totalWithTax = applyTax(discounted, taxRate);
    
    // JS float formatting constraints rounding accurately safely to decimals
    return Math.round(totalWithTax * 100) / 100;
}

// --- Unit Tests (Acceptance Criteria bounds) ---

function runTests() {
    // Test 1: Empty Array handling returns 0
    assert.strictEqual(calculateTotal([], 0.1, "NONE"), 0);

    // Test 2: Standard item calculation (No Discount)
    let items = [{price: 10, quantity: 2}, {price: 5, quantity: 1}]; // Math = subtotal 25
    assert.strictEqual(calculateTotal(items, 0.1, "NONE"), 27.50);

    // Test 3: Standard calculation with discount applied
    // Breakout: Subtotal 25 -> SAVE10 = 22.50 -> 10% tax = 24.75 
    assert.strictEqual(calculateTotal(items, 0.1, "SAVE10"), 24.75);

    // Test 4: Floating point fractional limit bounds check with discount mapping
    items = [{price: 10.99, quantity: 3}]; // Subtotal 32.97
    // Breakout: SAVE10 -> 29.673 -> Tax 5% -> 31.15665 -> Returns 31.16 correctly adjusted
    assert.strictEqual(calculateTotal(items, 0.05, "SAVE10"), 31.16);

    // Test 5: Only strict discount parsing mapped with explicitly 0 tax rate
    items = [{price: 50, quantity: 2}]; // Subtotal 100
    assert.strictEqual(calculateTotal(items, 0, "SAVE10"), 90.00);

    console.log("✅ Validation Completed: Task 2 Refactor & All 5 automated unit tests universally passed!");
}

// Run unit tests contextually 
if (require.main === module) {
    runTests();
}

module.exports = { calculateTotal, calculateSubtotal, applyDiscount, applyTax };
