# Python Function


# def myfunction():
#     print("This is a function")
# myfunction()


def num_validate(prompt):
    num = input(prompt)
    while not num.isnumeric():
        print("Error! Invalid number")
        num = input("Please enter valid number: ")
    return float(num)  # Convert to flaot and return


def getinput():
    # Check if numeric
    num1 = num_validate("Please enter first number: ")
    num2 = num_validate("Please enter second number: ")

    # while not num1.isnumeric():
    #     print("Error! Invalid number")
    #     num1 = input("Please enter a valid first number: ")
    # while not num2.isnumeric():
    #     print("Error! Invalid number")
    #     num2 = input("Please enter a valid second number: ")

    # Convert to Float
    # num1 = float(num1)
    # num2 = float(num2)

    oper = input("Please choose Operation (+,-,/,*): ")
    op = ["+", "-", "/", "*"]
    while oper not in op:
        print("Error Invalid Operand")
        oper = input("Please select a valid Operation (+,-,/,*): ")

    return num1, num2, oper


def myfunc01(num1, num2, oper):
    if oper == "+":
        ans = num1 + num2
    elif oper == "-":
        ans = num1 - num2
    elif oper == "/":
        ans = num1 / num2
    elif oper == "*":
        ans = num1 * num2
    print("The answer is " + str(ans))


r = "yes"
while r == "yes":
    num1, num2, oper = getinput()  # Capture returned value
    myfunc01(num1, num2, oper)
    # print(num1)
    # print(num2)
    # print(oper)

    r = input("want to repeat: yes? ")

print("The program has ended")
