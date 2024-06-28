
def greet():
    print("Greetings Mr. Sachin, Welcome to the event........")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.........")

# cty is called default argument and gname is a non default argument
def greetGstCty(gname, x, cty = "Mumbai"):
    print(f"Greetings {gname} from {cty}, Welcome to the event........{x}")

greet()
print("-" * 60)

greetGst("Rahul")
greetGst("Sehwag")

print("-" * 60)
greetGstCty("Rohit", "hello")
greetGstCty("Gavaskar", 25)
greetGstCty("Rahul", 50, "Bangalore")

print("-" * 60)
def add(x, y):
    # print(x + y)
    return x + y        # last line of code in the function


res = add(10, 20)
print(res)

print("-" * 60)
def diff(a, b):
    print(a - b)
    diff(a*2 - b*1)

