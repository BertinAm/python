# Day33: 50daysofcodechallenge
def inter_section(list1, list2):       # creating the function inter_section
    set1 = set(list1)           # converting list1 into a set called set1
    set2 = set(list2)           # converting list2 into a set called set2
    new_set = set1.intersection(set2)   # performing intersection between set1 and set2 using the intersection method
    new_list = list(new_set)   # converting new_set into a list
    sorted_list = sorted(new_list)  # sorting the newly created list new_list
    new_tuple = tuple(sorted_list)  # converting the list into a tuple called new_tuple
    return new_tuple    # printing out the tuple new_tuple


print(inter_section([20, 30, 60, 65, 75, 80, 85], [42, 30, 80, 65, 68, 88, 95]))    # calling the function inter_section


