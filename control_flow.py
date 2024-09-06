# calculation of a discount price using a function
def calculate_discount(price, discount_percent):
    original_price = price

    if discount_percent >= 20:
        discount_percentage = (original_price * discount_percent) / 100
        discount_price = original_price - discount_percentage
        print(f'You qualify for a discount of {discount_percentage:.2f}.')
        return discount_price
    else:
        print(f'You do not qualify for a discount.')
        return original_price

# Testing the function
price = float(input('Enter the price: '))
discount_percent = float(input('Enter the discount percentage: '))
print(f'The discount price is: {calculate_discount(price, discount_percent):.2f}')