num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(f"{num1} {operator} {num2}: {num1 + num2}")
elif operator == "-":
    print(f"{num1} {operator} {num2}: {num1 - num2}")
elif operator == "*":
    print(f"{num1} {operator} {num2}: {num1 * num2}")
elif operator == "/":
    print(f"{num1} {operator} {num2}: {num1 / num2}")
else:
    print("Invalid operator")