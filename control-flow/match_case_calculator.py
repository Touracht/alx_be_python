#
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case n if operation == "+":
        result = num1 + num2
        print("The result is", (result))
    case n if operation == "-":
        result = num1 - num2
        print("The result is", (result))
    case n if operation == "*":
        result = num1 * num2
        print("The result is", (result))
    case n if operation == "/":
        result = num1/num2
        print("The result is", (result))
    case n if num1 / 0:
        print("cannot divide by 0")
    case _:
        print("Not applicable!")
        #