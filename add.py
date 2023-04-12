import tabulate

# initialize an empty shopping list
shopping_list = []
"""
Add a new item to the shopping list.

This function prompts to enter the name, quantity, and price of an item,
creates a dictionary to represent the item with an auto-generated number of Item,
and appends the dictionary to the shopping list.
"""

def add_item():

    # get item name from user input
    while True:
        name = input("   Enter item name: ").lower()
        if name.isnumeric():
            print("   ---Please enter a text input for the item name.---")
        else:
            break
    
    # get item quantity from user input
    while True:
        try:
            qty = int(input("   Enter item quantity: "))
            break
        except ValueError:
            print("   ---Please enter a numeric input for the quantity.---")

    # get item price from user input
    while True:
        try:
            price = float(input("   Enter item price: "))
            break
        except ValueError:
            print("   ---Please enter a numeric input for the price.---")
            
    # generate new item number
    item_id = len(shopping_list) + 1

    # calculate total price of the item
    total_price = qty * price

     # create dictionary to represent item and append to the shopping list
    shopping_list.append({
        'no': item_id,
        'name': name,
        'quantity': qty,
        'price': price,
        'total price': total_price
    })

    # print a success message
    print("=" * 60)
    print(f"   Item added successfully.\n")

