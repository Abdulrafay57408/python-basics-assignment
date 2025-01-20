bill = int(input("Enter Bill Amount: "))
people = int(input("No. of People: "))

print(f"\nTotal Bill: ${bill} \nNo. of People: {people}\nEach Person Pays: ${bill//people}")