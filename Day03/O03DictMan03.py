
print("get".center(60, "-"))
player = {'name': 'sachin', 'runs': 145, 'age': 32, 'oppn': 'Zim', 'venue': 'chepauk'}
print(f"player :{player}")

print("-" * 60)
print(f"Name :{player.get('name', 'Please enter a valid key.....')}")
# print(f"Runs :{player['run']}")
print(f"Runs :{player.get('run', 'Please enter a valid key.....')}")

print("fromkeys".center(60, "-"))
# convert the list into a dictionary
cities = ['blr', 'che', 'mum', 'kol', 'hyd', 'del']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")
# set a default value to the cities
res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
# only add new key value pairs into the dictionary

emp = {'empid': 123, 'empname': 'Micheal', 'dept': 'finance', 'desig': 'MGR'}
print(f"emp :{emp}")

# modify
emp.setdefault('empname', 'George')
emp.setdefault('dept', 'Administration')

# add new
emp.setdefault('salary', 135000)
emp.setdefault('location', 'Mumbai')

print(f"emp :{emp}")

print("pop".center(60, "-"))
player = {'name': 'sachin', 'runs': 145, 'age': 32, 'oppn': 'Zim', 'venue': 'chepauk'}
print(f"player :{player}")

print("-" * 60)
res = player.pop('age')
print(f"res :{res}")

res = player.pop('venue')
print(f"res :{res}")

# res = player.pop()

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'sachin', 'runs': 145, 'age': 32, 'oppn': 'Zim', 'venue': 'chepauk'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

