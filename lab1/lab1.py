import calculator as c

class Calculator:
    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def subtract(slef, m, n):
        return c.subtract(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def gcd(self, m, n):
        return c.gcd(m, n)

instance = Calculator()

try:
    print("\nSum1: " + str(instance.sum(270, 192)))
    print("Sum2: " + str(instance.sum(270, -192)))
    #print("Sum3_error: " + str(instance.sum(27.5, -192))) # identico in tutte le operazioni.
    print("Subtraction1: " + str(instance.subtract(270, 192)))
    print("Subtraction1: " + str(instance.subtract(-270, 192)))
    print("Multiply1: " + str(instance.multiply(7, 2)))
    print("Multiply2: " + str(instance.multiply(7, -2)))
    print("Multiply3: " + str(instance.multiply(-7, -2)))
    print("Divide1: " + str(instance.divide(7, 2)))
    print("Divide2: " + str(instance.divide(0, 2)))
    print("Divide3: " + str(instance.divide(7, 0)))
    print("Divide4: " + str(instance.divide(0, 0)))
    print("GCD1: " + str(instance.gcd(270, -192)))
    print("GCD2: " + str(instance.gcd(0, 192)))
    print("GCD3: " + str(instance.gcd(270, 0)))
    print("GCD4: " + str(instance.gcd(0, 0)) + "\n")
except Exception:
    print("\nErrore!!\n")