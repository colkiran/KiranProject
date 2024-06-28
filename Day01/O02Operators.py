
"""
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Ternary Operators
"""

print("Arithmetic Operators".center(60, "-"))
print(f"sum  10 + 3 = {10 + 3}")
print(f"diff 10 - 3 = {10 - 3}")
print(f"mul  10 * 3 = {10 * 3}")
print(f"div  10 / 3 = {10 / 3}")
print(f'flrdiv 10 // 3 = {10 // 3}')
print(f"modulus 10 % 3 = {10 % 3}")
print(f"Exponential 10 ** 3 = {10 ** 3}")

print("Augmentor".center(60, "-"))
# =, +=, -=, /=
x = 5
print(f"x :{x}")

x += 10  # x = x + 10
print(f"x :{x}")

x /= 5    # x = x / 5
print(f"x :{x}")

print("Comparison Operators".center(60, "-"))
# ==, >, >=, <, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"2 == 1 :{2 == 1}")

print(f"1 > 2 :{1 > 2}")
print(f"1 < 2 :{1 < 2}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print("-" * 60)

print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print("-" * 60)

print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")
print("-" * 60)

# integer representation of unicode characters
print(f"ord('a') :{ord('a')}")  # ascii values
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")
print("-" * 60)

# ternary operator
age = 25
print("Eligible" if age > 18 else "Not Eligible")
