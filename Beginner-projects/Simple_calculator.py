# Simple Calculator
# Defining functions
# Addition
def add(n1, n2):
  return n1 + n2

# Subtraction
def sub(n1, n2):
  return n1 - n2

# Multiplication
def multiply(n1, n2):
  return n1 * n2 

# Division 
def div(n1, n2):
  return n1 / n2

# We keep the operations functions in a dictionary
operations = {
   "+": add,
   "-": sub,
   "*": multiply,
   "/": div,
}

# We make all this code into a function called calculator so that we can call the function again to allow the user to start over
def calculator():
  print(logo)
  # First number input using int
  num1 = float(input("What is the first number? "))

  #Loops the operations and prompts user to choose from the list
  for key in operations:
    print(key)
  operation_key = input("Please pick an operation by writing it from the list above: ")
  chosen_operation = operations[operation_key]
  #Second input
  num2 = float(input("What is the second number? "))
  # Picks the answer by using the chosen_operation and calculating the two numbers using that operation
  answer = chosen_operation(num1, num2)

  # Prints answer in an f-string
  print(f"{num1} {operation_key} {num2} = {answer} ")

  # As long as this variable is true, the program will loop.
  should_continue = True
  while should_continue == True: 
    user_input = input(f"Type 'y' if you want to continue calculating with {answer}, type 'n' to start a new calculation or type 'x' to exit the program. ").lower()
    # If user picks 'yes'
    if user_input == "y":
      #All this code is basically repeat from above
      operation_two = input("Pick an operation: ")
      chosen_operation = operations[operation_two]
      n3 = float(input("What's the next number? "))
      previous_answer = answer
      answer = chosen_operation(answer, n3)
      print(f" {previous_answer} {operation_two} {n3} = {answer} ")
    # If user picks 'no'
    elif user_input == "n":
      should_continue = False
      calculator()
    # If user types something else
    else:
      break

calculator()


# Lessons learned:
# You can put check for inputs in an if statement directly 
# Code could have been shorter and more readable if looped after the first number was chosen
