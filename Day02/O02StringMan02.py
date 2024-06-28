
# String manipulation functions

print("find".center(60, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
pos = st1.find("w")
print(f"position :{pos}")

print("-" * 60)
pos = st1.find("l")
print(f"position :{pos}")

# pos = st1.find("l", 3)
pos = st1.find("l", st1.find("l")+1)
print(f"position :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"position :{pos}")

print("replace".center(60, "-"))
print(f"st1 :{st1}")

# replace h with H
new_st = st1.replace("h", "H")
print(new_st)

print("-" * 60)
new_st = st1.replace("l", "L")
print(new_st)

print("-" * 60)
new_st = st1.replace("l", "L", 1)
print(new_st)

print("-" * 60)
new_st = st1.replace("l", "L", 2)
print(new_st)

print("index".center(60, "-"))
print(f"st1 :{st1}")

idx = st1.index("w")
print(idx)

print("-" * 60)
# idx = st1.index("a")
# print(idx)

pos = st1.find("a")
print(pos)

