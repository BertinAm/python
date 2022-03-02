num = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
for number in num:
    if number >= 75:
        print("Your mark is", number, "\t With a grade of First")
    if number >= 70 and number < 75:
        print("Your mark is ",number, "\t With a grade of Upper second")
    if number >= 60 and number < 70:
        print("Your mark is ",number, "\t With a grade of Second")
    if number >= 50 and number < 60:
        print("Your mark is ",number, "\t With a grade of Third")
    if number >= 45 and number < 50:
        print("Your grade is ",number, "\t With a grade of F1 supp")
    if number >= 40 and number < 45:
        print("Your mark is ", number, "\t With a grade of F2")
    if number < 40:
        print("Your mark is ",number, "\t With a grade of F3")
    else:
        pass
