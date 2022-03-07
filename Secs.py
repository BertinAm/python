def to_secs(hour, minutes, secs):
    value1 = hour * 3600
    value2 = minutes * 60
    n_secs = value1 + value2 + secs
    total_secs = int(n_secs)
    return "They are ", total_secs, "seconds in total"


print(to_secs(float(input("Enter any number of hours \n")), float(input("Enter any number of minutes \n")),
      float(input("Enter any number of seconds \n"))))
