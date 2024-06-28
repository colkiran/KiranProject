# nested functions

def outerFun():
    gname =  "Sachin"               # local varaible
    def innerFun():
        # only local variable can be converted into a nonlocal variable
        nonlocal gname
        gname = gname + " Tendulkar"
        print("Hello World")
        print(f"Greetings {gname}")

    # outerfunction scope
    innerFun()
    print(f"outerfun after :{gname}")


outerFun()