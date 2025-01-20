num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))


print(f"\nNumber 1: {num1}\nNumber 2: {num2} ")


print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}") if num2 > num1 else print(f"{num1} and {num2} are equal.")


print(f"Both numbers are Even") if (num1 % 2 == 0 and num2 % 2 == 0) else print(f"Both numbers are Odd") if (num1 % 2 != 0 and num2 % 2 != 0) else print(f"Both numbers are Mixed")