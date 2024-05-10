def add(x,y):
    result = x + y
    print("The sum of ",x," and ",y," is ",result)

def subtract(x,y):
    result = x - y
    print("The difference of ",x," and ",y," is ",result)

def multiply(x,y):
    result = x * y
    print("The product of ",x," and ",y," is ",result)


def division(x,y):
    result = x / y
    print("The quotient of ",x," and ",y," is ",result)



def calculator():
    op = input("Select operation: add, subtract, multiply, or divide: ")
    
    x = user_input_x()
    y = user_input_y()


    if (op == "add") or (op == "Add") or (op == "ADD"):
        add(x,y)

    elif (op == "subtract") or (op == "Subtract") or (op == "SUBTRACT"):
        subtract(x,y)

    elif (op == "multiply") or (op == "Multiply") or (op == "MULTIPLY"):
        multiply(x,y)

    elif (op == "divide") or (op == "Divide") or (op == "DIVIDE"):
        division(x,y)
    
    else:
        print("Could not register operation, please try again.")
        calculator()


def user_input_x():
    x = input("Enter first number: ")
    try:
        x = int(x)
    except:
        print("Input must be an integer.")
        x = user_input_x()
    return x

def user_input_y():
    y = input("Enter second number: ")
    try:
        y = int(y)
    except:
        print("Input must be an integer.")
        y = user_input_y()
    return y


calculator()
