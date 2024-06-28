
print("keys".center(60, "-"))

player = {'name': 'sachin', 'runs': 145, 'age': 32, 'oppn': 'Zim', 'venue': 'chepauk'}
print(f"player :{player}")

print("-" * 60)
k = player.keys()
print(f"k :{k}")

for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))

player = {'name': 'sachin', 'runs': 145, 'age': 32, 'oppn': 'Zim', 'venue': 'chepauk'}
print(f"player :{player}")

v = player.values()
print(v)

print("items".center(60, "-"))
emp = {
    'emp1': {'empid': 124, 'empname': 'Mike', 'age': 32, 'dept': 'finance', 'loc': 'Chennai', 'desig': 'MGR', 'salary': 185000},
    'emp2': {'empid': 145, 'empname': 'Jenny', 'age': 29, 'dept': 'MLT', 'loc': 'Delhi', 'desig': 'BDE', 'salary': 65000},
    'emp3': {'empid': 345, 'empname': 'Richard', 'age': 23, 'dept': 'IT', 'loc': 'Bangalore', 'desig': 'Developer', 'salary': 75000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
print(f"Name :{emp['emp1']['empname']}")

print("-" * 60)
for ky, dct in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in dct.items():
        print(k, "=>", v)
    print("-" * 60)

"""
ky = 'emp1'
info = {'empid': 124, 'empname': 'Mike', 'age': 32, 'dept': 'finance', 'loc': 'Chennai', 'desig': 'MGR', 'salary': 185000}

k, v = info.items()

"""

print("-" * 60)
print("-" * 60)

for k, v in emp['emp1'].items():
    print(k, "=>", v)

print("-" * 60)
dpt = emp['emp1']['dept']
print(dpt)

print("-" * 60)
ky = ['dept', 'age', 'desig']

for k in emp.keys():
    for i in ky:
        print(emp[k][i])
    print("-" * 60)

