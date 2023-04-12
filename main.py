import add
import update
import delete
import check
import reset
import payment
import total_price
import random
from datetime import datetime

"""
This is a cashier system program that helps customers 
to add, update, delete, show, and checkout items, calculate total price, and exit the program. 
It has a user-friendly interface and allows customers to make purchases efficiently. 
The program utilizes various functions for each option in the menu and can handle exceptions when the user inputs incorrect values.
The program also generates a unique transaction ID for each customer.
"""

print("=" * 60)
print(f"--------------- Welcome to Andi's Supermarket --------------")
print(f"---------------- Self Service Cashier System ---------------")
print("=" * 60)

# Asking the customer to enter their name and validating the input
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    else:
        print("Invalid input. Please enter alphabetic characters only.")

# Generating a unique transaction ID for each customer
transaction_id = "TX" + str(random.randint(1000, 9999))

# Getting the current date and time
current_date = datetime.now()
date = current_date.strftime("%d/%m/%Y %H:%M:%S")

# Printing the customer's details and transaction ID
print(f"\n   Name    : {name}")
print(f"   Date    : {date}")
print(f"   TX ID   : {transaction_id}")
print("=" * 60)

# Adding items to the list
print("\n---ADD ITEM")
while True:
    add.add_item()
    print("=" * 60)
    more_items = input("   Add more items? (y/n): ").lower()
    if more_items == "n":
        break

# Displaying the item menu for the customer
while True:
    print("=" * 60)
    print("\n   Item Menu")
    print("   1. Add Item")
    print("   2. Update item")
    print("   3. Delete item")
    print("   4. Show all items")
    print("   5. Reset items")
    print("   6. Calculate total price")
    print("   7. Checkout")
    print("   8. Exit\n")

    try:
        print("=" * 60)
        choice = int(input("   Enter your choice: "))
    except ValueError:
        print("   ---Invalid choice. Please enter a number.---")
        continue

    print("=" * 60)
    if choice == 1:
        print("\n   ADD ITEM\n")
        while True:
            add.add_item()
            more_items = input("   Add more items? (y/n): ").lower()
            print("\n")
            if more_items == "n":
                break
    elif choice == 2:
        print("---UPDATE ITEM")
        update_menu = True
        while update_menu:
            print("\n   1. Update item name")
            print("   2. Update item price")
            print("   3. Update item quantity")
            print("   4. Return to main menu")

            try:
                update_choice = int(input("\n   Enter your choice: "))
            except ValueError:
                print("\n   ---Invalid choice. Please enter a number.---\n")
                continue

            # Execute user's update choice
            if update_choice == 1:
                print("\n--UPDATED LIST OF ITEMS:")
                update.update_name()

            elif update_choice == 2:
                print("\n--UPDATED LIST OF ITEMS:")
                update.update_price()

            elif update_choice == 3:
                print("\n--UPDATED LIST OF ITEMS:")
                update.update_qty()

            elif update_choice == 4:
                update_menu = False

            else:
                print("   ---Invalid choice.---\n")

    elif choice == 3:
        print("---DELETE ITEM\n")
        delete_menu = True
        while delete_menu:
            print("   1. Delete Item")
            print("   2. Return to main menu")

            try:
                delete_choice = int(input("\n   Enter your choice: "))
            except ValueError:
                print("\n   ---Invalid choice. Please enter a number.---\n")
                continue

            # Execute user's update choice
            if delete_choice == 1:
                delete.delete_item()

            elif delete_choice == 2:
                delete_menu = False

            else:
                print("   ---Invalid choice.---\n")

    elif choice == 4:
        print("\n---SHOW ALL ITEMS\n")
        check.show_items()

    elif choice == 5:
        print("\n---RESET ITEMS\n")
        reset.reset_items()

    elif choice == 6:
        print("\n---CALCULATE TOTAL PRICE")
        total_price.calculate_price()

    elif choice == 7:
        print("---CHECKOUT ITEMS\n")
        checkout_menu = True
        while checkout_menu:
            print("   1. Yes")
            print("   2. No")

            try:
                checkout_choice = int(input("   Are you sure you want to checkout? "))
            except ValueError:
                print("\n   ---Invalid choice. Please enter a number.---")
                continue

            # Execute user's checkout choice
            if checkout_choice == 1:
                payment.checkout_items()
                print("============= Thank you for shopping with us! ==============")
                print("=" * 60)
                reset.reset_items()
                checkout_menu = False

            elif checkout_choice == 2:
                checkout_menu = False

            else:
                print("   ---Invalid choice.---\n")

    elif choice == 8:
        exit_menu = True
        while exit_menu:
            print("\n---Exit Menu\n")
            print("   1. Yes")
            print("   2. No\n")

            try:
                exit_choice = int(input("   Are you sure you want to exit? "))
            except ValueError:
                print("\n   ---Invalid choice. Please enter a number.---\n")
                continue

            if exit_choice == 1:
                print("=" * 60)
                print("============= Thank you for shopping with us! ==============")
                print("=" * 60)
                exit()

            elif exit_choice == 2:
                exit_menu = False

            else:
                print("   ---Invalid choice.---\n")

    else:
        print("   ---Invalid choice.---\n")
