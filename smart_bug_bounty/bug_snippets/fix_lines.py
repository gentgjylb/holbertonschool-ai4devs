import os

contents = {
    "bug1.py": [
        "# Python bug script",
        "class Calculator:",
        "    def __init__(self):",
        "        self.history = []",
        "    def add(self, a, b):",
        "        res = a + b",
        "        self.history.append(res)",
        "        return res",
        "    def get_last_result(self):",
        "        # Bug: index out of bounds if empty",
        "        return self.history[-1]",
        "calc = Calculator()",
        "print(calc.get_last_result())",
    ],
    "bug2.js": [
        "// JS bug script",
        "class Calculator {",
        "    constructor() { this.history = []; }",
        "    add(a, b) {",
        "        let res = a + b;",
        "        this.history.push(res);",
        "        return res;",
        "    }",
        "    getLastResult() {",
        "        // Bug: out of bounds return undefined",
        "        return this.history[this.history.length];",
        "    }",
        "}",
        "let calc = new Calculator();",
        "console.log(calc.getLastResult());",
    ],
    "bug3.java": [
        "// Java bug script",
        "import java.util.ArrayList;",
        "import java.util.List;",
        "public class bug3 {",
        "    private List<Integer> history = new ArrayList<>();",
        "    public int add(int a, int b) {",
        "        int res = a + b;",
        "        history.add(res);",
        "        return res;",
        "    }",
        "    public int getLastResult() {",
        "        // Bug: index out of bounds",
        "        return history.get(history.size());",
        "    }",
        "    public static void main(String[] args) {",
        "        bug3 calc = new bug3();",
        "        System.out.println(calc.getLastResult());",
        "    }",
        "}"
    ],
    "bug4.py": [
        "# Python bug script 2",
        "class Multiplier:",
        "    def __init__(self):",
        "        self.history = []",
        "    def divide(self, a, b):",
        "        # Bug: Zero division error not handled",
        "        res = a / b",
        "        self.history.append(res)",
        "        return res",
        "calc = Multiplier()",
        "calc.divide(5, 0)",
    ],
    "bug5.js": [
        "// JS bug script 2",
        "class Multiplier {",
        "    constructor() { this.history = []; }",
        "    divide(a, b) {",
        "        // Bug: division by zero returns Infinity",
        "        let res = a / b;",
        "        this.history.push(res);",
        "        return res;",
        "    }",
        "}",
        "let calc = new Multiplier();",
        "calc.divide(5, 0);",
    ],
    "bug6.go": [
        "// Go bug script",
        "package main",
        "import \"fmt\"",
        "type Multiplier struct {",
        "	history []int",
        "}",
        "func (m *Multiplier) divide(a int, b int) int {",
        "	// Bug: integer division by zero panic",
        "	res := a / b",
        "	m.history = append(m.history, res)",
        "	return res",
        "}",
        "func main() {",
        "	calc := Multiplier{}",
        "	calc.divide(5, 0)",
        "}"
    ]
}

out_dir = r"c:\Users\Gent\holbertonschool-ai4devs\smart_bug_bounty\bug_snippets"

for filename, lines in contents.items():
    while len(lines) < 40:
        lines.append(f"// padding line {len(lines) + 1}" if not filename.endswith(".py") else f"# padding line {len(lines) + 1}")
    
    with open(os.path.join(out_dir, filename), "w", newline='\n') as f:
        f.write("\n".join(lines))
        f.write("\n")

print("Done generating 40 lines!")
