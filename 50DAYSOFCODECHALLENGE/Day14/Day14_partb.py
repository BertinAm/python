# Day14_partb: 50daysofcodechallenge
def your_salary(name, numberofperiods, rate):
    if numberofperiods <= 100 and rate == 20:
        monthly_salary = numberofperiods * rate
        monthly_s = str(monthly_salary)
        c = monthly_s[0]
        d = monthly_s[1:]
        return "Teacher: %s " % name + "\n" + f"Periods: {numberofperiods} " + "\n" + f"Gross Salary: %s,%s" % (c, d)
    elif numberofperiods > 100 and rate == 25:
        monthly_salary = numberofperiods * rate
        monthly_s = str(monthly_salary)
        c = monthly_s[0]
        d = monthly_s[1:]
        return "Teacher: %s " % name + "\n" + f"Periods: {numberofperiods} " + "\n" + f"Gross Salary: %s,%s" % (c, d)


x = input("Enter your name \n")
y = int(input("Enter the number of periods \n"))
z = int(input("Enter the rate \n"))
print(your_salary(x, y, z))

