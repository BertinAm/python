# Day32: 50daysofcodechallenge
print(
    "Enter a password (it should be greater than or equal to 8 , it should have at least a lower case letter and an upper case letter)")


def password_validator(a):
    while True:
        emp = []
        emm = []
        epp = []
        for x in a.split():
            o = len(a)
        for y in a:
            b = y.islower()
            c = str(b).count("True")
            emp.append(c)
        for z in a:
            d = z.isupper()
            f = str(d).count("True")
            emm.append(f)
        for g in a:
            p = g.isnumeric()
            j = str(p).count("True")
            epp.append(j)

        if o >= 8:
            if emp.count(1) >= 1:
                if emm.count(1) >= 1:
                    if epp.count(1) >= 1:
                        return a
                    else:
                        print("There must be at least a number in your password")
                        return password_validator(input("Enter a password \n"))
                else:
                    print("There must be at least an uppercase letter in your password")
                    return password_validator(input("Enter a password \n"))
            else:
                print("There must be at least a lowercase letter in your password")
                return password_validator(input("Enter a password \n"))
        else:
            print("Your password is less than 8 characters")
            return password_validator(input("Enter a password \n"))


print(password_validator(input("Enter a password \n")))
