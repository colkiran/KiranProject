
# namedtuple is like immutable dictionary
from collections import namedtuple

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("ArithmeticCalc", "s d p q")
    arith = nmdTpl(s = sum, d = diff, p = prod, q = quot)
    return arith

ar = arithmeticCalc(20, 8)
print(ar)
print(f"Sum  :{ar.s}")
print(f"Diff :{ar.d}")
print(f"Prod :{ar.p}")
print(f"Quot :{ar.q}")
