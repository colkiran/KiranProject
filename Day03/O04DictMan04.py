
emp1 = {'empid': 124, 'empname': 'Mike', 'age': 32, 'dept': 'finance', 'loc': 'Chennai', 'desig': 'MGR'}

emp2 =  {'empid': 145, 'empname': 'Jenny', 'age': 29, 'dept': 'MLT', 'loc': 'Delhi', 'salary': 65000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)

print(f"emp1 :{emp1}")

print("clear".center(60,"-"))
emp2 =  {'empid': 145, 'empname': 'Jenny', 'age': 29, 'dept': 'MLT', 'loc': 'Delhi', 'salary': 65000}

print(f"emp2 :{emp2}")
emp2.clear()

print(f"emp2 :{emp2}")

print("copy".center(60, "-"))
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"d1 before :{d1}")

# copy dictionary d1 into d2
d2 = d1     # shallow copy - copies the address with the data
print(f"d2 before :{d2}")

d2[6] = 'f'
d2[7] = 'g'
d2[8] = 'h'

print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("=" * 60)
print("=" * 60)

d3 = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
print(f"d3 before :{d3}")

# copy the dictionary d3 to d4
d4 = d3.copy()      # deep copy - copying only the data
print(f'd4 before :{d4}')

d4['d'] = 'dog'
d4['e'] = 'egg'
d4['f'] = 'frog'

print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("=" * 60)
print("=" * 60)

d5 = {'name': 'sachin', 'runs':{'odi': 24500, 'test': 18450}, 'age': 36}
print(f"d5  before :{d5}")

# copy dictionary d5 to d6
d6 = d5.copy()
print(f"d6 before :{d6}")

d6['runs']['t20'] = 2500

print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

print("=" * 60)
print("=" * 60)

from copy import deepcopy
d7 = {'name': 'zaheer', 'age': 32, 'wickets': {'pak': 185, 'sri': 150, 'aus': 120}}
print(f"d7 before :{d7}")

# copy the dictionary d7 to d8
d8 = deepcopy(d7)
print(f"d8 after :{d8}")

d8['wickets']['eng'] = 78
d8['wickets']['nzl'] = 60
d8['wickets']['zim'] = 38

print(f"d8 after :{d8}")
print(f"d7 after :{d7}")
