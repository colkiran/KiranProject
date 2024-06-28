
glbX = 100

def fun(x):              # x is a local variable
    global glbX          # do not assign any value in this line
    print(f"x :{x}")
    glbX = 250
    print(f"inside :{glbX}")
    y = 15
    print(f"y :{y}")

print(f"glbX before :{glbX}")

fun(10)

print(f"glbX after :{glbX}")

