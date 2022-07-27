# Day34: 50daysofcodechallenge
def just_digits(file):    # defining the function called just_digits
    read_file = file.read()    # parsing the read python.csv file into a variable called read_csv
    list1 = list(read_file.split())   # converting the string read_file into a list called list1
    list_of_numbers = []   # creating an empty list
    for read_list in list1:    # iterating through list1 and storing the values in a variable named read_list
        if read_list.isnumeric():   # checking the variable read_list to see if they are any numbers
            list_of_numbers.append(int(read_list))  # storing the numbers into a new list called list_of_numbers
    return list_of_numbers  # printing out this list of numbers found


print(just_digits(file=open("python.csv", "r")))  # calling the function just_digits
