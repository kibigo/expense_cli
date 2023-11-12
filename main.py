import sqlite3
import datetime

conn = sqlite3.connect('expense.db')
cur = conn.cursor()

user_and_password = {}

def create_account():
    print("Create a new account")
    username = input("Enter the Username: ")
    password = input("Enter the password: ")
    user_and_password[username] = password
    print("Account successfully created")


def login(username, password):
    if username in user_and_password and user_and_password[username] == password:
        return True
    else:
        return False

def add_expense():
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    description = input("Enter the description of the expense: ")

    cur.execute("SELECT DISTINCT category FROM expense")

    categories = cur.fetchall()

    print("Select a category by number:")

    for index, category in enumerate(categories):
        print(f"{index + 1}. {category[0]}")

    print(f"{len(categories) + 1}. Create a new category")

    category_choice = int(input())

    if category_choice == len(categories) + 1:
        category = input("Enter the new category name: ")

    else:
        category = categories[category_choice -1][0] 

    price = input("Enter the price of the expense: ")

    cur.execute("INSERT INTO expense(Date, description, category, price) VALUES (?, ?, ?, ?)", (date, description, category, price))

    conn.commit()

def view_expense():
    cur.execute("SELECT * FROM expense")
    expenses = cur.fetchall()
    for expense in expenses:
        print(expense)

def view_by_month():
    month = input("Enter the month (MM): ")
    year = input("Enter the year (YYYY): ")

    cur.execute("""SELECT category, SUM(price) FROM expense 
                WHERE strftime('%m', Date) = ? AND strftime('%Y', Date)= ?
                GROUP BY category""", (month, year))
            
    expenses = cur.fetchall()
    for expense in expenses:
        print(f"Category: {expense[0]}, Total: {expense[1]}")


def main():

    while True:

        print("Welcome to Expense system")
        print("1. Log in")
        print("2. Create account")

        expense_choice = int(input())

        if expense_choice == 1:
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            if login(username, password):

                while True:


                    print("Select an option:")
                    print("1. Enter a new expense")
                    print("2. View expenses summary")

                    choice = int(input())

                    if choice == 1:
                        add_expense()

                    elif choice == 2:

                        print("Select an option:")
                        print("1. View all expenses")
                        print("2. View monthly expenses by category")

                        view_choice = int(input())

                        if view_choice == 1:
                            view_expense()


                        elif view_choice == 2:
                            view_by_month()

                        else:
                            print("Invalid choice.")


        elif expense_choice == 2:
            create_account()
    
if __name__ == "__main__":
    main()