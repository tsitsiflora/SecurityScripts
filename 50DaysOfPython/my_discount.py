# Write a function that takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount.

def my_discount():
    price = int(input("Enter the price: "))
    disc = int(input("Enter the discount: "))

    price_after_discount = price - (disc/100 * price)
    return price_after_discount


print(my_discount())