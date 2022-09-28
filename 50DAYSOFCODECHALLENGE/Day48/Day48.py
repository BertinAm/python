# Day48: 50daysofcodechallenge
def binary_search(list1, value):    # defining our function
    low = 0   # storing the index of the first element in the variable low
    high = len(list1) - 1   # storing the index of the last element in the variable high
    mid = 0  # creating a variable with value 0
    while low <= high:   # checking if the lower index is less than or equal to the higher index
        mid = (low + high) // 2  # dividing the usm of the lower and upper index by 2 to obtain the mid-index
        if value < list1[mid]:   # checking if the value at the mid-index is greater than the value entered by the user
            high = mid - 1  # changing the value of the upper index
        elif value > list1[mid]:  # checking if the value entered by the user is greater than the value at the mid-index
            low = mid + 1  # changing the value of the lower index
        else:
            return mid  # returning mid-index if the above conditions are not met
    return -1  # return -1 if the lower index becomes higher than the upper index


numbers = [12, 34, 56, 78, 98, 22, 45, 13]  # creating a list called numbers with a length of 8
result = binary_search(sorted(numbers), int(input("Enter the number you wish to search \n")))  # calling the binary_search function

if result != -1:  # checking if the function is different from -1
    print(f"index {result}")   # printing the index of the searched element
else:
    print("Element doesn't exit")

