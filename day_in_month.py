def day_in_month(month):
    if month == "January":
        print("31 Days")
    elif month == "February":
        print("28 Days")
    elif month == "March":
        print("31 Days")
    elif month == "April":
        print("30 Days")
    elif month == "May":
        print("31 Days")
    elif month == "June":
        print("30 Days")
    elif month == "July":
        print("31 Days")
    elif month == "August":
        print("31 Days")
    elif month == "September":
        print("30 Days")
    elif month == "October":
        print("31 Days")
    elif month == "November":
        print("30 Days")
    elif month == "December":
        print("31 Days")
    else:
        print("Invalid Entry")
    return "Howdy!"


print(day_in_month(input("Enter a the name of any month with the first letter in capital and the rest in lowercase" 
                         " and see how many days it has \n")))
