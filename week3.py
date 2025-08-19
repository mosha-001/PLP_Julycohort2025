def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount.
    Only apply the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main Program ---
# Prompt user for inputs
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
