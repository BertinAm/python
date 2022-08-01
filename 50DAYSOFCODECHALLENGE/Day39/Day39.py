# Day39: 50daysofcodechallenge
print("Welcome to my password generator am called Ben \n")
print(
    "If you want a strong password enter strong \t if you want a weak password enter week \t if you want a very strong password enter very strong ")


def generate_password(word):     # creating the function generate_password
    import random       # importing the random module
    import string       # importing the string module

    punctuation_symbols = string.punctuation     # using the punctuation method of the string module
    lowercase_letters = string.ascii_lowercase   # using the ascii_Lowercase method of the string module
    uppercase_letters = string.ascii_uppercase   # using hte ascii_uppercase method of the string module
    numbers = string.digits                      # using the digit method of the string module
    if word == "weak":                  # checking if the word entered by the user is equal to weak
        bb = random.sample(punctuation_symbols, 2)  # generating random punctuation symbols of length 2 and using the sample method of the random module
        dd = random.sample(lowercase_letters, 1)    # generating random lowercase letters of length 1 and using the sample method of the random module
        hh = random.sample(uppercase_letters, 1)    # generating random uppercase letters of length 1 and using the sample method of the random module
        nn = random.sample(numbers, 1)      # generating random digits of length 1 and using the sample method of the random module

        final1 = bb + dd + hh + nn    # performing concatenation
        for tt in final1:     # performing iteration
            print(tt, end="")   # printing the variable tt

    elif word == "strong":          # checking if the word entered by the user is equal is strong
        b = random.sample(punctuation_symbols, 2)
        d = random.sample(lowercase_letters, 2)
        h = random.sample(uppercase_letters, 2)
        n = random.sample(numbers, 2)

        final = b + d + h + n
        for t in final:    # performing iteration
            print(t, end="")   # printing the variable t

    elif word == "very strong": # checking if the word entered by the user is very strong
        bbb = random.sample(punctuation_symbols, 3)
        ddd = random.sample(lowercase_letters, 3)
        hhh = random.sample(uppercase_letters, 3)
        nnn = random.sample(numbers, 3)
        final2 = bbb + ddd + hhh + nnn  # performing concatenation
        for ttt in final2:   # performing iteration
            print(ttt, end="")  # printing the variable ttt
    else:
        generate_password(input("What type of password do you want? \n").lower())


generate_password(input("What type of password do you want? \n").lower())
