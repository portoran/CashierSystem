import total_price
from add import shopping_list
"""
This function calculates the total price, discount, and discounted price of items in a shopping list.
It then prompts the user to enter a payment amount and calculates the change.
"""
def checkout_items():
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

    # Calculate discount amount and discounted price
    discount_amount = total_price * discount
    discounted_price = total_price - discount_amount
    
    print("=" * 60)
    print(f"   Total Price All Item: Rp. {total_price}")
    print(f"   Discount: {discount * 100}%")
    print(f"   Discount Amount: Rp. {discount_amount}")
    print(f"\n   Discounted Price: Rp. {discounted_price}")
    print("=" * 60)

    # Prompt the user for payment
    while True:
        try:
            payment = float(input("   Enter payment amount: "))
        except ValueError:
            print("=" * 60)
            print("   ---Invalid input. Please enter a number.---")
            print("=" * 60)
            continue
        
        if payment < discounted_price:
            print("=" * 60)
            print("   ---Insufficient payment. Please enter a larger amount.---")
            print("=" * 60)
        else:
            break
    
    # calculate change
    change = payment - discounted_price
    print(f"   Changes: Rp. {change:.1f}")
    print("=" * 60)

