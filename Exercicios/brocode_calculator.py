user_operation_choice = input("What operation would you like to do (+ - * /): ")

num1 = float(input("Type the numbers:\n"))
num2 = float(input())

if user_operation_choice == "+":
    result = num1 + num2
    print(f"Result: {result:.3f}")

elif user_operation_choice == "-":
    result = num1 - num2
    print(f"Result: {result:.3f}")

elif user_operation_choice == "*":
    result = num1 * num2
    print(f"Result: {result:.3f}")

elif user_operation_choice == "/":
    result = num1 / num2
    print(f"Result: {result:.3f}")

else:
    print(f"{user_operation_choice} is not a valid operator")
