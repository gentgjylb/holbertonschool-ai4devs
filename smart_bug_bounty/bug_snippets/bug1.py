# Python bug script
class Calculator:
    def __init__(self):
        self.history = []
    def add(self, a, b):
        res = a + b
        self.history.append(res)
        return res
    def get_last_result(self):
        # Bug: index out of bounds if empty
        return self.history[-1]
calc = Calculator()
print(calc.get_last_result())
# padding line 14
# padding line 15
# padding line 16
# padding line 17
# padding line 18
# padding line 19
# padding line 20
# padding line 21
# padding line 22
# padding line 23
# padding line 24
# padding line 25
# padding line 26
# padding line 27
# padding line 28
# padding line 29
# padding line 30
# padding line 31
# padding line 32
# padding line 33
# padding line 34
# padding line 35
# padding line 36
# padding line 37
# padding line 38
# padding line 39
# padding line 40
