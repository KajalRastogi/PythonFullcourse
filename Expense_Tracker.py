"""Mini Project:
question: create a console-based expense tracker program in python that allows the user to record daily expenses and view summaries like total spending.
using concepts upto 7 days.
project details: you are required to build a simple personal finance management tool. the program should allow the user to:
. add an expense with details like date,category, description,and amount.
.view all recorded expenses in a clean format.,calculate total spending so far.,exit the program gracefully when the user chooses to.
 All tasks must be implemented using loops,if-else,lists, and dictionaries only .No user-defined functions or file handling should be used.

Welcome To Expense Tracker
 menu : add expense, view all expenses, view total spending, exit
enter your choice(1-4):1
Enter date(DD-MM-YYYY): 05-11-2025"""


expenseslist =[] #list of all expenses (in form of dictionary)
print("-------Welcome To Expense Tracker------")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total spend money")
    print("4. Exit")

    Choice = int(input("Enter your choice:"))
# Add Expense
    if Choice== 1:
        date = input("Enter your date:")
        category = input("Enter your category? (food,travel,makeup,books,clothes etc..):")
        description = input("Enter your details of category:")
        amount = float(input("Enter your amount:"))

        expense = {
            "date": date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenseslist.append(expense)
        print("\n Expense is added successfully!")
# view all expenses
    elif Choice== 2:
        if len(expenseslist)==0:
           print("No Expenses added yet.")
        else:
            print("===your all expense===")
            Count = 1
            for eachexpense in expenseslist:
                print(f"expense number {Count} --> {eachexpense['date']},{eachexpense['category']},{eachexpense['description']},{eachexpense['amount']}")
                Count += 1

#view total spending 
    elif Choice== 3:
        total=0
        for eachexpense in expenseslist:
            total = total+eachexpense["amount"]
        print("\n Total Expense =",total)
#Exit
    elif Choice== 4:
        print("Thankyou for coming")
        break

    else:
        print("Invalid Choice! Try Again")

