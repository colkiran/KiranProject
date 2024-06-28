
st1 = "******hello******"

print("lstrip".center(60, "-"))
print(f"st1 :{st1}")

res = st1.lstrip("*")
print(f"res :{res}")

print("rstrip".center(60, "-"))
print(f"st1 :{st1}")

res = st1.rstrip("*")
print(f"res :{res}")

print("strip".center(60, "-"))
print(f"st1 :{st1}")

res = st1.strip("*")
print(f"res :{res}")

print("isnumeric".center(60, "-"))
st1 = "hello123world"
st2 = "1234india4321"

res = st1[5].isnumeric()
print(res)
print("-" * 60)
#extract india from the string
print(f"st2 :{st2}")

for i in range(0, len(st2)):
    if not(st2[i].isnumeric()):
        print(st2[i], end="")
print()

# print(st2[4:9])

# translate, maketrans
print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = "helowrd"
b = "HELOWRD"
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)

print(f"res :{res}")
