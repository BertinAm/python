# Day6: 50daysofcodechallenge
email = input("Enter your email \n")   # Enter your email

for username in email:
    if username == "@":   # checking for @ in the string entered by the user
        break      # ending the check
    print(username, end="")    # printing the string without the @gmail.com



