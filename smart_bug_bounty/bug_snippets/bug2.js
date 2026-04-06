// A class to manage a simple shopping cart and calculate totals
// Applies discounts to items based on promo codes.

class ShoppingCart {
    constructor() {
        this.items = [];
        this.discountCodes = {
            'SAVE10': 0.10,
            'SAVE20': 0.20,
            'HALFOFF': 0.50
        };
        this.appliedDiscount = 0;
    }

    addItem(name, price, quantity) {
        this.items.push({ name, price, quantity });
    }

    applyDiscountCode(code) {
        if (this.discountCodes[code]) {
            this.appliedDiscount = this.discountCodes[code];
            return true;
        }
        return false;
    }

    calculateTotal() {
        let subtotal = 0;
        // Bug: using `in` instead of `of` for arrays iterates over indices, so item is an index string.
        for (let item in this.items) {
            subtotal += item.price * item.quantity;
        }

        let discountAmount = subtotal * this.appliedDiscount;
        // Bug: precision error, but more importantly above bug causes subtotal to be NaN
        let total = subtotal - discountAmount;
        
        return {
            subtotal: subtotal.toFixed(2),
            discount: discountAmount.toFixed(2),
            total: total.toFixed(2)
        };
    }
}

// Test the shopping cart
const cart = new ShoppingCart();
cart.addItem("Laptop", 1200.00, 1);
cart.addItem("Mouse", 45.00, 2);
cart.applyDiscountCode("SAVE10");
const receipt = cart.calculateTotal();
console.log(receipt);
