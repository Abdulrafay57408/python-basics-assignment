city1 = input("Enter the name of 1st city: ")
tem1 = int(input("Enter the temperature of 1st city: "))

city2 = input("Enter the name of 2nd city: ")
tem2 = int(input("Enter the temperature of 2nd city: "))


print(f"\n{city1} is hotter than {city2}") if tem1 > tem2 else print(f"\n{city2} is hotter than {city1}")