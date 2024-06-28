
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

# print("-" * 60)
# x = {1: 100, 2: 200, 3: 300},
# print(x)
# print(type(x))

print("-" * 60)
t1 = (1, 2, 3, 4, 5)
print(f"t1[2] :{t1[2]}")
# t1[2] = 250
# immutable

print("-" * 60)
# print(dir(t1)) - count, index

t2 = (1, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 1, 1, 1)

# count
print(f"1 :{t2.count(1)}")
print(f"2 :{t2.count(2)}")
print(f"3 :{t2.count(3)}")

print("-" * 60)
# index
print(t2.index(3))
print(t2.index(3, t2.index(3) + 1))
