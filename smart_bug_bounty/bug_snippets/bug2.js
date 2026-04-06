// bug2.js
// Intended behavior: Manage a shopping cart that accumulates items,
// applies a promo discount code, and returns a correct receipt total.

class ShoppingCart {
    constructor() {
        this.items = [];
        this.discountCodes = {
            'SAVE10':  0.10,
            'SAVE20':  0.20,
            'HALFOFF': 0.50,
        };
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

        // Bug: `for...in` iterates over array *indices* (strings "0", "1", …),
        // not the item objects. So `item.price` and `item.quantity` are both
        // `undefined`, making subtotal = NaN for every operation.
        for (let item in this.items) {
            subtotal += item.price * item.quantity;
        }

        const discountAmount = subtotal * this.appliedDiscount;
        const total = subtotal - discountAmount;

        return {
            subtotal:  subtotal.toFixed(2),
            discount:  discountAmount.toFixed(2),
            total:     total.toFixed(2),
        };
    }
}

// Test the shopping cart
const cart = new ShoppingCart();
cart.addItem("Laptop", 1200.00, 1);
cart.addItem("Mouse",     45.00, 2);
cart.applyDiscountCode("SAVE10");

const receipt = cart.calculateTotal();
console.log("Receipt:", receipt);
