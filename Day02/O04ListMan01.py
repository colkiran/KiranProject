
l1 = list()     # list() is a function that creates an empty list
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l1 = [1, 2, 3, 'four', 'five ', 'six', 7.0, 8.3, 9.1, True, False, 12+0j, 13-2j, 14j]
print(f"l1 :{l1}")
print(type(l1))
print(type(l1[-2]))

print("-" * 60)
l3 = list(range(1, 11))
print(f"L3 :{l3}")

print("-" * 60)
values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

lst4 = [*lst1, *lst2]           # upack
print(f"lst4 :{lst4}")
print(len(lst4))
