def hide_password():           # defining the function that takes no parameters
    global new_password
    password = input("Enter your password \n")  # asking the usr to enter a password
    if len(password) > 0:     # checking if the length of the password is greater than zero
        new_password = '*' * len(password)  # multiplying the * times the length of the password
    return "Your password is", new_password, "and your password is", len(password), "characters long"


print(hide_password())    # calling the function hide_password



