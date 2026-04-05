const assert = require('assert');

const calculateSubtotal = items => items.reduce((sum, item) => sum + item.price * item.quantity, 0);

const applyDiscount = (subtotal, code) => code === 'SAVE10' ? subtotal * 0.9 : subtotal;

const applyTax = (amount, rate) => amount * (1 + rate);

const calculateTotal = (items = [], taxRate = 0, discountCode = "NONE") => {
    if (!items.length) return 0;
    const totalWithTax = applyTax(applyDiscount(calculateSubtotal(items), discountCode), taxRate);
    return Number(Math.round(totalWithTax + 'e2') + 'e-2'); 
};

assert.strictEqual(calculateTotal([], 0.1, "NONE"), 0);
assert.strictEqual(calculateTotal([{price: 10, quantity: 2}, {price: 5, quantity: 1}], 0.1, "NONE"), 27.50);
assert.strictEqual(calculateTotal([{price: 10, quantity: 2}, {price: 5, quantity: 1}], 0.1, "SAVE10"), 24.75);
assert.strictEqual(calculateTotal([{price: 10.99, quantity: 3}], 0.05, "SAVE10"), 31.16);
assert.strictEqual(calculateTotal([{price: 50, quantity: 2}], 0, "SAVE10"), 90.00);

console.log("AI Gen Task 2: All Auto-Scaffolded Tests Executing Flawlessly.");
module.exports = { calculateTotal, calculateSubtotal, applyDiscount, applyTax };
