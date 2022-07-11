def age_in_minutes(birth_year):  # defining the function age_in_minutes
    import time  # importing a library called time

    year = time.asctime()  # using the method asctime() to get the current date, time and year
    year_new = year.split()  # using the split method to separate the values obtained
    current_year = int(year_new[4])  # extracting the year from the str year_new
    while True:  # using a while statement
        empty = []  # defining an empty list called empty
        if len(birth_year) == 4 and 1900 <= int(
                birth_year) <= current_year:  # checking if the length of birth_year id exactly equal to 4 and if the birth year falls between 1900 and the current year we are in
            actual_age = current_year - int(birth_year)  # subtracting the current year from the birth_year
            actual_age_in_minutes = actual_age * 8760 * 60  # obtaining the number of minutes a person as lived up till the current year
            for age in str(actual_age_in_minutes):  # parsing actual_age_in_minutes to age
                empty.append(age)  # appending the values in age to the list empty
            if len(empty) == 8:  # checking if the length of the list empty is exactly equal to 8
                return ("You are " + empty[0] + empty[1] + "," + empty[2] + empty[3] + empty[4] + "," + empty[5] +
                        empty[6] + empty[7] + " minutes old")  # printing the year in minutes separated by comma's
            elif len(empty) == 7:
                return ("You are " + empty[0] + "," + empty[1] + empty[2] + empty[3] + "," + empty[4] + empty[5] +
                        empty[6] + " minutes old")
            elif len(empty) == 6:
                return ("You are " + empty[0] + "," + empty[1] + empty[2] + empty[3] + "," + empty[4] + empty[
                    5] + " minutes old")
            else:
                return "You are " + empty[0] + " minutes old"
            break
        if len(birth_year) < 4 or len(
                birth_year) > 4:  # checking if the length of the birth_year is less than or greater than 4
            print("Invalid Input!")
            time.sleep(1)  # delaying the execution of the next statement by 1 second
            birth_year = input("Enter your year of birth \n")  # asking the user to input their birth_yea
            continue  # keep asking  until they enter a correct year

        if int(birth_year) < 1900 or int(
                birth_year) > current_year:  # checking if the length of the birth year is less than 1900 and greater than the current_year
            print("Enter a valid year!")
            time.sleep(1)  # delaying the execution of the next statement by 1 second
            birth_year = input("Enter your year of birth \n")
            print(birth_year)
            continue


print(age_in_minutes(input("Enter your year of birth \n")))  # calling the function age_in_minutes
