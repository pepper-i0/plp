def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    else:
        return price

# QWuestion 2 
price = float(input("Enter the price:"))
discount_percent = float(input("Enter discount percentage:"))

final_price = calculate_discount(price, discount_percent)
print("final price is:", final_price)