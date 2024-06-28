
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

# def diff(x, y):
#     print(x - y)
#     diff(x*2, y*3)
#
# diff(20, 8)
def fact(n):
    if n == 0 or  n == 1:
        return 1
    else:
        return n * fact(n - 1)

x = 5
print(f"The factorial of {x} is :{fact(x)}")

print("-" * 60)
# how many values can a function return in python
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# variable length arguments (variable number arguments)
# *var can accept more than one value
def prodAll(*numbers):
    print(numbers)
    print(*numbers)    # unpack
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print("Multiply All = ", prodAll(1, 2, 3, 4, 5))


print("-" * 60)
# **var will accept data like a dictionary
def extract_detial(**details):
    # print(details)
    for k, v in details.items():
        print(k, "=>", v)


extract_detial(name="Sachin", age=34, runs=130, oppn="Aus", venue="perth")

print("-" * 60)
# docstrings
def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)      # __doc__ = double underscore = dunder_doc

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)

    1. if we pass both arguments ass integers then the function will return the sum of it
    2. if we pass both arguments as strings then the function will return the concatenated string
    3. if we pass one integer and one string as argument then the will throw an error
    """

    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))
# print(fun1(10, "world"))

print("-" * 60)
help(fun1)