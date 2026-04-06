// JS bug script 2
class Multiplier {
    constructor() { this.history = []; }
    divide(a, b) {
        // Bug: division by zero returns Infinity
        let res = a / b;
        this.history.push(res);
        return res;
    }
}
let calc = new Multiplier();
calc.divide(5, 0);
// padding line 13
// padding line 14
// padding line 15
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
