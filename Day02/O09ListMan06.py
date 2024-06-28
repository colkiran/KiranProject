"""
sort   - sorts the original list
sorted - take a copy of the list and sorts it and returns it
"""
l1 = [8, 5, 2, 9, 1, 4, 10, 3, 6, 7]
print(f"l1 :{l1}")

asc_res = sorted(l1)
print(f"Ascending  :{asc_res}")
desc_res = sorted(l1, reverse=True)
print(f"Descending :{desc_res}")

print("-" * 60)
l1 = [8, 'zebra', 'apple', 5, 'yellow', 'blue', 2, 'white', 'cat', 9, 1, 'violet', 'dog', 4, 'pink', 'green', 10, 'maroon', 'egg',  3, 'hen', 'xray',  6, 7, 118, 1076, 29, 250, 2174]
print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
cities = ['thiruvananthapuram', 'ooty', 'hyderabad', 'pune', 'mumbai', 'bangalore', 'chennai', 'delhi', 'kolkota']

print(f"cities :{cities}")
res = sorted(cities, key=len)
print(f"res :{res}")

print("reverse".center(60, "-"))

l1 = [8, 5, 2, 9, 1, 4, 10, 3, 6, 7]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")

