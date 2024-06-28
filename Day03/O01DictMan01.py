
player = {'name': 'Sachin', 'age': 32, 'runs': 80, 'oppn': 'Aus'}
print(f"player :{player}")
print(type(player))

print("-" * 60)
# 01 Create a dictionary
d1 = dict()         # creates an empty dictionary
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
# 02 Create a dictionary
player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': "Nzl"}
print(f"Player :{player}")
print(type(player))

print("-" * 60)
# 03 Create a dictionary
player = dict([('name', 'sehwag'), ('age', 28), ('runs', 58), ('oppn', 'Pak')])
print(f"player :{player}")
print(type(player))

print("-" * 60)
# 04 Create a dictionary
player = dict(name="Dhoni", age=30, runs=105, oppn='WI')
print(f"player :{player}")
print(type(player))

# CRUD operation
player = {'name': 'sachin', 'age': 35, 'runs': 125, 'oppn': 'WI'}
print(f"player :{player}")
print(type(player))

print("-" * 60)
# Read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"oppn :{player['oppn']}")

print("-" * 60)
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# Update - modify and add new key value into the dictionary
print(f"player :{player}")

# modification
player['name'] = "Sachin Tendulkar"
player['runs'] = 135

# new key value
player['venue'] = 'sabina park'
player['year'] = 2003

print(f"player :{player}")

# delete
print("-" * 60)
print(f"player :{player}")
del player['age']
del player['year']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
