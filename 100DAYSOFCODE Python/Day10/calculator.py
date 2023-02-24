# Day10 100DaysOfCodePython
# Calculator

from art import logo
# Calculator

# function to add 2 numbers
def add(n1, n2):
      # return n1 + n2
  return n1 + n2


# function to subtract 2 numbers
def subtract(n1, n2):
      # return n1 - n2
  return n1 - n2

# function to multiply 2 numbers
def multiply(n1, n2):
      # return n1 * n2
  return n1 * n2

# function to divide 2 numbers
def divide(n1,  n2):
      # return n1 / n2
  return n1 / n2

# dictionary to store the functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
# function to calculate the result
def calculator():
      # printing the logo
  print(logo)
  # taking the first number from the user
  num1 = float(input("What's the first number?: "))
  # asking the user to pick an operation
  operation_symbol = input("Pick an operation from the line above: ")
  # taking the second number from the user
  num2 = float(input("What's the second number?: "))
  # iterating through the dictionary to print the operations
  for symbol in operations:
    print(symbol)
  
  # subsetting the dictionary to get the function
  calculation_function = operations[operation_symbol]
  # calling the function and storing the result in a variable called answer
  answer = calculation_function(num1, num2)
  
  # printing the result
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  # creating a variable called statement to store the boolean value
  statement = True
  # creating a while loop to ask the user if they want to continue
  while statement:
        # asking the user if they want to continue
    operation_symbol = input("Pick an operation: ")
    # taking the next number from the user
    num3 = float(input("Enter another number: "))
    # subsetting the dictionary to get the function
    calculation_function = operations[operation_symbol]
    # calling the function and storing the result in a variable called next_answer
    next_answer = calculation_function(answer, num3)
    # printing the result
    print(f"{answer} {operation_symbol} {num2} = {next_answer}")
    # asking the user if they want to continue
    response = input("Do you which to continue 'yes' or 'no'\n")
    # if the user enters yes, the answer variable will be assigned the next_answer variable
    if response == "yes":
          # assigning the next_answer variable to the answer variable
      answer = next_answer
    # if the user enters no, the statement variable will be assigned False
    else:
      statement = False
      # calling the calculator function
      calculator()

# calling the calculator function   
calculator()
  
