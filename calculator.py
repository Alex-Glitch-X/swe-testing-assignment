class Calculator:
    def __init__(self):
        self.result = 0
        self.current_input = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def clear(self):
        self.result = 0
        self.current_input = 0
        return self.result
