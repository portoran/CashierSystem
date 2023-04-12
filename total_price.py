from add import shopping_list
import tabulate
"""
The code calculates the total price of items in the shopping list, 
applies a discount based on the total price, and prints a summary of the shopping list, 
total price, discount, discount amount, and discounted price. 
The summary is printed in a tabular format using the tabulate library.

"""

def calculate_price():
    total_price = 0
    for item in shopping_list:
        total_price += item['price'] * item['quantity']
    
    discount = 0

    # determine discount percentage based on total price
    if total_price > 500000:
        discount = 0.1
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05

    print(tabulate.tabulate(shopping_list, headers='keys', tablefmt='fancy_grid'))

    discount_amount = total_price * discount # calculate discount amount
    discounted_price = total_price - discount_amount # calculate discounted price
    
    # print summary of total price, discount, discount amount, and discounted price
    print("=" * 60)
    print(f"   Total Price All Item: Rp. {total_price}")
    print(f"   Discount: {discount * 100}%")
    print(f"   Discount Amount: Rp. {discount_amount}")
    print(f"\n   Discounted Price: Rp. {discounted_price}")
    print("=" * 60)
