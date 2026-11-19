print("================================")
print("     STUDENT EXPENSE TRACKER")
print("================================")

budget = float(input("Enter your monthly budget: "))

total = 0

while True:

    print("\n1. Add Expense")
    print("2. View Total Expenses")
    print("3. Check Remaining Budget")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        amount = float(input("Enter today's expense: "))

        total = total + amount

        print("Expense added successfully!")

    elif choice == "2":

        print("Total expenses: Rs.", total)

    elif choice == "3":

        remaining = budget - total

        print("Remaining budget: Rs.", remaining)

        if remaining < 0:
            print("You have exceeded your budget!")

        else:
            print("You are within your budget!")

    elif choice == "4":

        print("Thank you for using the tracker!")
        break

    else:
        print("Invalid choice!")
