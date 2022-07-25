# Day33_partb: 50daysofcodechallenge
import time   # importing the time module

range_of_numbers = range(10000000)    # creating a range of numbers from 0 to 10000000 using the range function
set1 = set(range_of_numbers)   # creating a set called set1 from the range of numbers
list1 = list(range_of_numbers)  # creating a list from the range of numbers
number = int(input("Enter a you wish to find"))  # asking the user to input a number
start = time.time()    # parsing the start time of code snippet below into a variable called start
if number in set1:    # checking if the number entered by the user is in the set called set1
    print(number)   # printing out the number if it was found in the range of numbers
else:
    print("not found")  # if the number wasn't found print not found
stop = time.time()     # parsing the end time of the code snippet above into a variable called stop
print(start - stop)  # printing the time it took for the code snippet in between the variables start and stop to run

begin = time.time()    # parsing the start time of code snippet below into a variable called begin
if number in list1:      # checking if the number entered by the user is in the list called list1
    print(number)    # printing out the number if it was found in the range of numbers
else:
    print("not found")  # if the number wasn't found print not found
end = time.time()   # parsing the end time of the code snippet above into a variable called end
print(begin - end)   # printing the time it took for the code snippet in between the variables begin and end to run
print("From the above code snippet it shows that the list takes more time to compile compared to the set")
