# T(n) = 3T(n/2) + O(n) Time Complexity: O(n^1.585)   Space Complexity: O(n)
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)-ac-bd
    return ac * (10 ** (2 * m)) + abcd * (10 ** m) + bd
x=123432
y=635678
print(karatsuba(x,y))