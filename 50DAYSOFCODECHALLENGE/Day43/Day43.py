# Day43: 50daysofcodechallenge
def student_marks():  # declaring the function student_marks
    dict1 = {}   # creating an empty dictionary
    while True:  # setting the condition for the while loop as True
        names = input("Enter your name or done \n")  # asking the user to enter the name of the student
        if names == "done":  # checking if the name entered by the user is equal to done
            break   # breakout of the loop if the condition is met
        else:
            marks = int(input("Enter your marks \n"))   # asking the user to enter the students mark
            dict1[names] = marks    # parsing the values for a corresponding name and mark into the dictionary
    print(dict1) # printing the dictionary


student_marks()  # calling the function


