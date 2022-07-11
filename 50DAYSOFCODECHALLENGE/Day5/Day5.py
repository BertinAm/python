# Day5: 50daysofcodechallenge
def my_discount():     # declaring the function
    price = int(input("Enter the price $"))         # asking the user for the price
    discount = int(input("Enter the discount \n"))      # asking the user for the input
    price_after_discount = price - ((discount / 100) * price)   # calculating the price after the discount
    return price_after_discount         # returning the price after the discount


print(my_discount())






