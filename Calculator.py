class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adder(self):
        return self.x + self.y
    
    def subtractor(self):
        return self.x - self.y

    def multiplier(self):
        return self.x * self.y
    
    def divider(self):
        return self.x / self.y

    def clear(self):
        self.x = 0
        self.y = 0


inpt1 = int(input("Enter the first number: "))
inpt2 = int(input("Enter the second number: "))
calc = Calculator(inpt1, inpt2)
print(f"Adding two numbers: {calc.adder()}")
print(f"Subtracting two numbers: {calc.subtractor()}")
print(f"Multiplying two numbers: {calc.multiplier()}")
print(f"Dividing two numbers: {calc.divider()}")
print(f"resetting numbers!")
calc.clear()
print(f"x is now {calc.x} and y is {calc.y}")

