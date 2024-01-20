# Single Comment

"""
The quick brown fox jump over the lazy dog
"""

print("this is a sample of text display")


x = 1
x1 = 2
y = 2.0
z = True
a = "example"


print(type(x))
print(type(y))
print(type(z))
print(type(a))

# True - higher value ; False - lower value
# Addition
print(x + z)
print(x + False)

# Concatenation
print(str(x) + a)
print("x" + a)

# print(x + int(a)) - error
print(x + int(len(a)))

print(5**2)


# modulo
remainder_modulo = 8 % 2
print(remainder_modulo)

# check next line and qoute
print("dir\\'\nx")


# INSERT INFORMATION
# print(input("Enter Value: "))
1
# enter a value:
# Addition
"""num1 = float(input("Enter First Value: "))
num2 = float(input("Enter Second Value: "))
zz = num1 + num2"""
# print(zz)

"""print(type(num1))
print(type(num2))"""


# = setting a value
# == questioning a value (True or False)
# != Not equal to


x01 = 7
if x01 < 7:
    print("True")
else:
    print("False")


"""
AND - ASSUME MULTIPLICATION (1X0 = 0)

X1      CONDITION   X2      OUTPUT
FALSE   AND         FALSE   FALSE
FALSE   AND         TRUE    FALSE
TRUE    AND         FALSE   FALSE
TRUE    AND         TRUE    TRUE

OR - ASSUME ADD (>1 = TRUE)
FALSE   OR          FALSE   FALSE
FALSE   OR          TRUE    TRUE
TRUE    OR          FALSE   TRUE
TRUE    OR          TRUE    TRUE


"""

"""
A001 = 7
B001 = 5

if A001 < 7 and B001 == 5:
    print("True")
elif A001 > 7 and B001 != 5:
    print("True")
else:
    print("False")

"""

"""

A001 = 7
B001 = 5

print("True") if A001 == 2 else print("False")




# for loop
# while

x = ["a", "b", "c"]
for y in x:
    print(y)



for xa in range(10):
    print("The Value is: " + str(xa))

    


def myfunction():
print("Run")
pass


myfunction()
"""


x = ["a", "b", "c", "d", "e", "f", "g"]
letter = "f"


"""for y in x:
    # print(y)
    # print(type(x))
    if y == letter:
        # print(y)
        print("Match found")
        # pass
        break
    else:
        # print(y)
        print("No match")
        # pass

    # break
    # print("Check end")"""
i = 0

while i < len(x):
    print(x[i])
    i += 1
