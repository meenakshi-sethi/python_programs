# Simple Expense Tracker 

#program allows you to track your expenses and view the total amount spent.

# initiating list to store all expense records
expenses = []

# creating a function to add new exp
def add_expense():
    item = input("Enter name of item: ").strip()
    if not item: # check if the item name is empty
        print("Item name cannot be empty. Please try again")
        return
    try:
        cost = float(input("Enter cost of item: ")) #convert cost to a float
        if cost < 0: # ensure cost is non negative
            print("Cost cannot be negative. Please enter a valid amount.")
            return
        expenses.append({"item": item, "cost": cost}) # store the expense as a dictionary in the list
        print(f"Added:{item} - ${cost:.2f}")
    except ValueError:
        print("Invalid cost. Please enter a numeric value.")
    
# creating a function to display all recorded expenses and calculates the total spending
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    print("\nYour Expenses: ")
    total = 0 # variable to calculate total cost
    for expense in expenses:
        print(f"{expense['item']}: ${expense['cost']:.2f}")
        total += expense['cost'] # adding each expense to total
    print(f"Total Spent: ${total: .2f}\n")

# main function to display menu and handle user choices
def main():
    while True:
        print("\nExpense Tracker Menu: ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                add_expense() # call add_expense function
            elif choice == 2:
                view_expenses() # call view view_expenses function
            elif choice == 3:
                print("Thank you for using the Expense Tracker. Bye!")
                break #to exit program
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid number.")

# Run program
if __name__ == "__main__":
    print("Welcome to the Simple Expense Tracker!")
    main()