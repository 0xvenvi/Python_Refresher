print("Mathematical Operation")

r = "yes"
while r == "yes":
    x = input("Please enter first number: ")

    """ Other Code
    if x.isnumeric():
        x = float(x)
    else:
        x = input("Please enter a valid number: ")
    """

    # Check for Numeric
    while not x.isnumeric():
        x = input("Please enter a valid number: ")

    y = input("Please enter second number: ")
    while not y.isnumeric():
        y = input("Please enter a valid number: ")

    # Convert to Float
    x = float(x)
    y = float(y)

    # Check for Operation
    op = ["+", "-", "/", "*"]
    z = input("Please choose Operation (+,-,/,*): ")
    while z not in op:
        z = input("Please select a valid Operation (+,-,/,*): ")

    if z == "+":
        ans = x + y
    elif z == "-":
        ans = x - y
    elif z == "/":
        ans = x / y
    elif z == "*":
        ans = x * y

    """   
    #Other Code
    op = False
    while op == False:
        # Check Chosen Mathematical Operation
        z = input("Please choose Operation (+,-,/,*): ")
        if z == "+":
            ans = x + y
            op = True
        elif z == "-":
            ans = x - y
            op = True
        elif z == "/":
            ans = x / y
            op = True
        elif z == "*":
            ans = x * y
            op = True
        else:
            print("Please input correct value for Mathematical Operation")
            op = False
    
    """

    print("The answer is " + str(ans))
    r = input("want to repeat: yes? ")

print("The program has ended")
