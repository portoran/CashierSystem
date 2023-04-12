import tabulate
from add import shopping_list

def update_name():
    """
    Updates the name of an item in the shopping list.
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("   Enter number of item to update: "))
            break
        except ValueError:
            print("   ---Invalid item number. Please enter a number.---")
    new_name = input("   Enter new item name: ")

    for item in shopping_list:
        if item['no'] == item_id:
            item['name'] = new_name
            break

    print("=" * 60)
    print("   Item updated successfully.")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))

def update_price():
    """
    Updates the price of an item in the shopping list.
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("   Enter number of item to update: "))
            break
        except ValueError:
            print("---Invalid item number. Please enter a number.---")
    new_price = float(input("   Enter new item price: "))

    for item in shopping_list:
        if item['no'] == item_id:
            item['price'] = new_price
            break

    print("=" * 60)
    print("   Item updated successfully.")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))

def update_qty():
    """
    Updates the quantity of an item in the shopping list.
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("   Enter number of item to update: "))
            break
        except ValueError:
            print("   ---Invalid item number. Please enter a number.---")
    new_qty = int(input("   Enter new item quantity: "))

    for item in shopping_list:
        if item['no'] == item_id:
            item['quantity'] = new_qty
            break
        
    print("=" * 60)
    print("   Item updated successfully.\n")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))
