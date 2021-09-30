import calculator as c

class Calculator:
    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

instance = Calculator()
print("sum:" + str(instance.sum(1, -3)))

