// bug2.js – ShoppingCart with for...in iteration bug
class ShoppingCart {
    constructor() {
        this.items = [];
        this.discountCodes = { 'SAVE10': 0.10, 'SAVE20': 0.20 };
        this.appliedDiscount = 0;
    }
    addItem(name, price, quantity) {
        this.items.push({ name, price, quantity });
    }
    applyDiscountCode(code) {
        if (this.discountCodes[code] !== undefined) {
            this.appliedDiscount = this.discountCodes[code];
            return true;
        }
        return false;
    }
    calculateTotal() {
        let subtotal = 0;
        // Bug: for...in on an array yields index strings ("0","1",...)
        // not the element objects. item.price and item.quantity are
        // both undefined so every multiplication returns NaN.
        for (let item in this.items) {
            subtotal += item.price * item.quantity;
        }
        const discountAmount = subtotal * this.appliedDiscount;
        const total = subtotal - discountAmount;
        return {
            subtotal: subtotal.toFixed(2),
            discount: discountAmount.toFixed(2),
            total:    total.toFixed(2),
        };
    }
}

const cart = new ShoppingCart();
cart.addItem("Laptop", 1200.00, 1);
cart.addItem("Mouse", 45.00, 2);
cart.applyDiscountCode("SAVE10");
console.log("Receipt:", cart.calculateTotal());
