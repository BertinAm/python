# Day47: 50daysofcodechallenge
def save_json():    # creating our function save_json
    import json as js  # importing the json library

    names = {'name': 'Carol', 'sex': 'female', 'age': 55}  # creating a dictionary called names with 3 keys
    json_object = js.dumps(names)    # creating a json object
    with open("dictionary.json", "a") as f:   # appending the json object to the json file
        f.write(json_object)  # writing to the json file


save_json()   # calling the function save_json


def read_json():  # creating a function read_json
    f = open("dictionary.json", "r")   # reading from the json file
    for file in f:   # iterating to the file
        print(file)  # printing the contents of the file


read_json()   # calling the function read_json


