# Day9: 50daysofcodechallenge
def biggest_odd(numbers):   # defining my function
    empty = [int(new_number) for new_number in numbers]   # applying list comprehension to list called empty
    empty_odd = [x for x in empty if x % 2 == 1]    # applying list comprehension to list called empty_odd
    return "The biggest odd number you entered is", max(empty_odd) # returning the biggest odd number


print(biggest_odd(input("Enter a set of numbers \n")))   # asking the user to input a number




