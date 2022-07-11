# Day8: 50daysofcodechallenge
def odd_even(number):  # creating the function  odd_even
    new_list = []  # creating an empty list
    new_list1 = number.split(",")  # splitting each number entered
    empty_list = []  # creating another empty list
    for new_list in new_list1:  # parsing the list to variable
        new_list = int(new_list)  # converting the variable to an integer
        empty_list.append(new_list)  # adding the list to the empty list
    even_list = []  # creating an empty list
    odd_list = []  # creating another empty list
    for new_int in empty_list:  # parsing the list to a variable
        if new_int % 2 == 0:  # comparing each element in the list to obtain the integers
            even_list.append(new_int)  # appending the variable to a list
            big_even = max(even_list)  # getting the biggest  even number in the list
        else:
            odd_list.append(new_int)  # appending the variable to another empty list
            big_odd = min(odd_list)  # getting the minimum / the smallest odd number
    subtract = big_even - big_odd  # subtracting the biggest even number from the smallest even number
    return subtract


print(odd_even(input("enter a list of numbers and after each number place a comer \n")))
