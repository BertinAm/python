def is_factor(f, n):
    if n % f == 0:
        return n, "is a factor of ", f
    else:
        return n, "is not a factor of ", f


print(is_factor(int(input("Enter a number \n")), int(input("Enter a number \n"))))
