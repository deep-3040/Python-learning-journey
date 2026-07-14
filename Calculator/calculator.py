############### Safe Mini Project ##############
# The calculator should:

# Ask for first number.
# Ask for second number.
# Ask for operator:
# +
# -
# *
# /
# Perform the calculation.
# Handle:
# ValueError
# ZeroDivisionError
try:
    a = int(input("Enter the 1st number: "))
    c = input("Choose an operator (+, -, *, /, %): ")
    b = int(input("Enter the 2nd number: "))
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    elif c == "%":
        print(a % b)
    else:
        print("Operator Galat hai")
except ValueError:
    print("input integer daalo")
except ZeroDivisionError:
    print("zero mat daalo bhai")
