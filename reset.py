from add import shopping_list
"""
Reset the shopping list by removing all items from it.
"""
def reset_items():
    confirm = input("   Are you sure you want to reset the shopping list? (y/n) ").lower()

    if confirm == 'y':
        shopping_list.clear()
        print("=" * 60)
        print("   ---Shopping list reset successfully.---")
    else:
        print("=" * 60)
        print("   ---Shopping list reset canceled.---")