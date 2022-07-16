# Day24: 50daysofcodechallenge
def average_calories(calories):
    from statistics import mean
    calories_list = calories.split(",")
    empty = []
    for c in calories_list:
        for d in c:
            empty.append(int(d))
    return f"Your average intake is: {mean(empty)}"


print(average_calories(input("Enter your calorie intake for any number of days and separate each by a comma\n")))
