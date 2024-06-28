"""
local variable are variable with lexical scope - losses its scope out of a block of code
"""
def fun(x):         # x is a local variable
    print(f"x :{x}")
    y = 250         # local variable
    print(f"y :{y}")


fun(10)
# print(f"x after :{x}")