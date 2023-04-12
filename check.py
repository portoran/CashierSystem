import tabulate
from add import shopping_list

def show_items():
    """
    Display the items in the shopping list.

    This function uses the tabulate library to format the shopping list as a table,
    with the item ID, name, quantity, and price displayed as columns.
    """
    
    if not shopping_list:
        print("=" * 60)
        print("   ---No items in shopping list.---")
        print("=" * 60)
    else:
        # use tabulate to format the shopping list as a table with headers
        print(tabulate.tabulate(shopping_list, headers='keys', tablefmt='fancy_grid'))
