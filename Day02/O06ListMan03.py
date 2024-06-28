
# CRUD - Create, Read, Update, Delete
l1 = list(range(1, 6))
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")

for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# update - modify, insert a new element
print(f"l1 :{l1}")
l1[0] = 11
l1[4] = 'five'

print(f"l1 :{l1}")
# insert new values
l1[1] = 2.5
l1[3] = 300
# l1[5] = 5.5
print(f"l1 :{l1}")

print("-" * 60)
# delete
del l1[4]
del l1[2]

print(f"l1 :{l1}")

print("append".center(60, "-"))
l1 = [10, 20, 30, 40, 50]
print(f"l1 :{l1}")

l1.append(60)
l1.append(70)
l1.append(80)

l1.append([90, 100, 110, 120, 130])

print(f"l1 :{l1}")
# print 100, 110, 120
print(f"l1[8] :{l1[8]}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("Extend".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l1 = [2, 4, 6, 8, 10]
print(f"l1 :{l1}")
l1.insert(1, 3)
l1.insert(3, 5)
l1.insert(5, 7)
l1.insert(7, 9)

print(f"l1 :{l1}")
