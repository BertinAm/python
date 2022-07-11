def hide_password():  # defining a function called hide_password()
    files = open("new_txt.txt", "r")      # reading from a file called new_txt
    for file in files:  # passing the contents through a for loop in other to read it line by line
        print(file)
    if len(file) > 0:   # checking if the contents of the file are greater than 0
        new_password = '*' * len(file)     # multiplying the length of the contents of the file by *
    return "Your password is", new_password, "and your password is", len(file), "characters long"


print(hide_password())   # calling the function





