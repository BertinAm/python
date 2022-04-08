from array import *

vals = array("i", [1, 2, 3, 4])   # creating an array vals with datatype int
NewArr = array(vals.typecode, (a * a for a in vals))  # creating a new array from the previous array vals
for i in NewArr:
    print(i)    # print the array 1 after another
