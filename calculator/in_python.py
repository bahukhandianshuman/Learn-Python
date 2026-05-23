def calculate(number1, operator, number2):
    if operator == '+':
        print(f"result: {number1 + number2}")
    elif operator == '-':
        print(f"result: {number1 - number2}")
    elif operator == '*':
        print(f"result: {number1 * number2}")
    elif operator == '/':
        if number2 == 0:
            print("cant divide by 0")
        else:
            print(f"result: {number1 / number2}")
    else:
        print("invalid operator, please use +, -, *, /")

print("welcome to calculator")
ret = True
while ret:
    try:
        number1 = float(input("enter number 1: "))
        operator = input("enter operator: ")
        number2 = float(input("enter number 2: "))
        calculate(number1, operator, number2)
    except ValueError:
        print("please enter a valid number")
        continue
    boolean = input("do you want to continue? ")
    ret = boolean == 'yes'

print("goodbye!")  # this runs when user says no