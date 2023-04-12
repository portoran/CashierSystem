import tabulate
from add import shopping_list

def delete_item():
    """
    Delete an item from the shopping list.

    This function prompts the user to enter the number of an item to delete,
    searches the shopping list for an item with that number,
    removes the item from the shopping list if found,
    and displays the updated shopping list.
    """
    # prompt user for number of item to delete
    print(tabulate.tabulate(shopping_list, headers='keys'))
    item_id = int(input("\n   Enter number of item to delete: "))

    # loop through shopping list and remove item with matching number
    for i, item in enumerate(shopping_list):
        if item['no'] == item_id:
            shopping_list.remove(item)

            # update item number's of the remaining items
            for j in range(i, len(shopping_list)):
                shopping_list[j]['no'] -= 1
            break

    # print success message and updated shopping list
    print("=" * 60)
    print("   ---Item deleted successfully.---")
    print("=" * 60)
    
    print(tabulate.tabulate(shopping_list, headers='keys'))
    print("\n")
