from art import logo
# Calculator

# function to add 2 numbers
def add(n1, n2):
  return n1 + n2


# function to subtract 2 numbers
def subtract(n1, n2):
  return n1 - n2

# function to multiply 2 numbers
def multiply(n1, n2):
  return n1 * n2

# Division
def divide(n1,  n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
  
  for symbol in operations:
    print(symbol)
  
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  statement = True
  while statement:
    operation_symbol = input("Pick an operation: ")
    num3 = float(input("Enter another number: "))
    calculation_function = operations[operation_symbol]
    next_answer = calculation_function(answer, num3)
    print(f"{answer} {operation_symbol} {num2} = {next_answer}")
    response = input("Do you which to continue 'yes' or 'no'\n")
    if response == "yes":
      answer = next_answer
    else:
      statement = False
      calculator()
      
calculator()
  
