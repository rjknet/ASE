# calculator

def sum(m, n):
    if type(m) is int and type(n) is int:
        result = m
        if(n > 0):          # set the initial sum value to m 
            while(n > 0):   # ad 1 to sum variable until n is != from 0
                result += 1    
                n -= 1
        else:
            while(n < 0):   # remove 1 to sum variable until n is != from 0
                result -= 1    
                n += 1
        return result
    else:
        raise Exception

def subtract(m, n):
    if type(m) is int and type(n) is int:
        result = m
        if(n > 0):
            while(n > 0):
                result -= 1
                n -= 1
        else:
            while(n < 0):
                result += 1
                n += 1
        return result
    else:
        raise Exception

def multiply(m, n):
    if type(m) is int and type(n) is int:
        result = 0
        if(m == 0 or n == 0):
            return result
        positive_result = m > 0 and n > 0 or m < 0 and n < 0
        m = abs(m)
        n = abs(n)
        while(n > 0):
            result += m
            n -= 1
        result = result if positive_result else -result
        return result
    else:
        raise Exception

def divide(m, n):
    if type(m) is int and type(n) is int:
        if(n == 0 and m != 0):
            return float('inf')
        elif(n == 0 and m == 0):
            return float('nan')
        elif(n != 0 and m == 0):
            return 0
        else:
            result = 0
            positive_result = (m > 0 and n > 0) or (m < 0 and n < 0)
            n = abs(n)
            m = abs(m)
            while(m >= n):
                result += 1         # each time m >= n, 1 is added to the result
                m = m - n
            result = result if positive_result else result
        return result           # the result of the division is in Z
    else:
        raise Exception

def gcd(m, n):  #5, 0
    if type(m) is int and type(n) is int:
        if(m == 0 and n != 0):
            return abs(n)
        elif(m == 0 and n == 0):
            return 0
        elif(m != 0 and n == 0):
            return abs(m)
        else:
            return gcd(n, m%n)
    else:
        raise Exception

def main():
    print("calculator:")
    print("sum: " + str(sum(4, -4)))
    print("division: " + str(divide(0, 0)))

"""
try:
    main();
except Exception:
    print("operation not in Z")
"""