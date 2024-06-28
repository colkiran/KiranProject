
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the elements of l1 to l2
l2 = l1             # shallow copy - copies the address along with data
print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy the elements of l3 to l4
l4 = l3.copy()          # deep copy - only the data gets copied
print(f"l4 before :{l4}")

l4.extend([11, 12, 13, 14])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)

l5 = [2, 4, 6, 8, [1, 2, 3, 4, 5], 10]
print(f"l5 before :{l5}")

# copy the elements of l5 to l6
l6 = l5.copy()      # deep copy
print(f"l6 before :{l6}")

l6[4].append(6)
l6[4].append(7)
l6[4].append(8)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)

from copy import deepcopy

l7 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l7 before :{l7}")

# copy l7 to l8
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[4].extend([60, 70, 80])

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")
