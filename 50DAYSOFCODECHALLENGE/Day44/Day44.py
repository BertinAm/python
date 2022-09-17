# Day44: 50daysofcodechallenge
def save_emails():  # creating the function save_email
    while True:  # setting the condition to True
        email = input("Enter your email or done\n")  # asking the user to enter his/her email
        if email == "done":  # checking if the email entered is done
            break   # breaking out of the loop
        else:
            f = open("emails.csv", "a")  # opening the csv file and appending to it
            f.write(f"{email}\n")  # writing to the csv file
    f.close()  # closing the csv file


save_emails()  # calling the function save_emails


def open_emails():  # creating the function open_email
    f = open("emails.csv", "r")    # opening and reading from the csv file
    for emails in f:  # iterating through the file
        print(emails)  # printing out the contents of the csv file


open_emails()  # calling the function open_email
