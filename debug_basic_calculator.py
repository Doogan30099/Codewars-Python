def calculate(a, o, b):
    try:
        if(o == "+"):
            return a + b
        elif(o == "-"):
            return a - b
        elif(o == "/"):
            return a / b
        elif(o == "*"):
            return a * b
        else:
            return None
    except:
        return None