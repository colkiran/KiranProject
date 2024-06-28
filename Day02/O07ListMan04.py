
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))

l2 = [1, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]

print(f'l2 :{l2}')
l2.remove(3)
print(f"l2 :{l2}")

l2.remove(3)
print(f"l2 :{l2}")

l2.remove(3)
print(f"l2 :{l2}")

while 2 in l2:
    l2.remove(2)

print(f"l2 :{l2}")

print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("index".center(60, "-"))
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'a']
print(f"l1 :{l1}")

print(l1.index('d'))

print(l1.index('a'))
print(l1.index('a', l1.index('a') + 1))

print("count".center(60, "-"))
l2 = [1, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]

print(f'l2 :{l2}')

print(f"1 :{l2.count(1)}")
print(f"2 :{l2.count(2)}")
print(f"3 :{l2.count(3)}")
print(f"8 :{l2.count(8)}")
