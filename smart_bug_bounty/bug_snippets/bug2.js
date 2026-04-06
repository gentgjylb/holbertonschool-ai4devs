// JS bug script
class Calculator {
    constructor() { this.history = []; }
    add(a, b) {
        let res = a + b;
        this.history.push(res);
        return res;
    }
    getLastResult() {
        // Bug: out of bounds return undefined
        return this.history[this.history.length];
    }
}
let calc = new Calculator();
console.log(calc.getLastResult());
// padding line 16
// padding line 17
// padding line 18
// padding line 19
// padding line 20
// padding line 21
// padding line 22
// padding line 23
// padding line 24
// padding line 25
// padding line 26
// padding line 27
// padding line 28
// padding line 29
// padding line 30
// padding line 31
// padding line 32
// padding line 33
// padding line 34
// padding line 35
// padding line 36
// padding line 37
// padding line 38
// padding line 39
// padding line 40
