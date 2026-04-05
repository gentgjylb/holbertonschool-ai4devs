const assert = require('assert');

const calculateSubtotal = items => items.reduce((total, {price, quantity}) => total + price * quantity, 0);
const applyDiscount = (subtotal, code) => code === 'SAVE10' ? subtotal * 0.90 : subtotal;
const applyTax = (amount, rate) => amount * (1 + rate);

const calculateTotal = (items = [], taxRate = 0, discountCode = "NONE") => {
    if (items.length === 0) return 0;
    const finalAmount = applyTax(applyDiscount(calculateSubtotal(items), discountCode), taxRate);
    return Number(Math.round(finalAmount + 'e2') + 'e-2'); 
};

// Unit execution assessments
assert.strictEqual(calculateTotal([], 0.1, "NONE"), 0);
assert.strictEqual(calculateTotal([{price: 5, quantity: 2}], 0.1, "NONE"), 11.00);
assert.strictEqual(calculateTotal([{price: 15, quantity: 2}], 0.1, "SAVE10"), 29.70);
assert.strictEqual(calculateTotal([{price: 10.99, quantity: 3}], 0.05, "SAVE10"), 31.16);
assert.strictEqual(calculateTotal([{price: 45, quantity: 1}], 0, "SAVE10"), 40.50);

console.log("All unit criteria for javascript pricing calculator passed successfully.");
module.exports = { calculateTotal, calculateSubtotal, applyDiscount, applyTax };
