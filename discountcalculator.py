def calculate_discount(price, discount_percent):
    """
    Function to calculate the final price after applying a discount.
    Applies discount only if discount_percent >= 20.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
