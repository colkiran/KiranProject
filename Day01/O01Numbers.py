
"""
int
float
complex
"""

a = 10
b = -10

print(f"a :{a}")        # format string - interpolation
print(type(a))          #RTTI = runtime type identification
print(f"b :{b}")
print(type(b))
print("The sum of {a} and {b} is {a + b}")
print("-" * 60)

c = 10.0
d = -10.0
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))
print("-" * 60)

e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))
print("-" * 60)

g = 3.14j
h = -3.14j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))
print("-" * 60)
print(max(10, 20, 30, 40))
print(min(10, 20, 30, 40))

print("-" * 60)
x = 2 + 3.5
print(type(x))

x = 2
y = 3.5
z = x + y
print(f"x =  {type(x)}")
print("y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)       # decimal number
print(0b11)     # binary number - 2 ** 1 + 2 ** 0 = 2 + 1
print(0b101)    # binary number 101  - 1 - 2**0, 0, 2**2 = 1 + 4
print(0o11)     # octal numbers
print(0o101)    # octal numbers
print(0o15)     # octal number
print(0xe)      # hexadecimal
print(0xa)      # hexadecimal

print("Number System Conversion".center(60, "-"))
a = 100
print(f"oct(100) :{oct(a)}")
print(f"bin(100) :{bin(a)}")
print(f"hex(100) :{hex(a)}")