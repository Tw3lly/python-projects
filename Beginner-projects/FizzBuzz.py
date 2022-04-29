# FizzBuzz
#Prints the number from 1 to 100
# If number is divisible by 3 it should print fizz
# If number is divisible by 5 it should print buzz
# If its divisible by both, it should print fizzbuzz
# Else, it should just print the number.
# Since the loop will go from top to bottom, we check if its divisible by both first 

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0:
        print("Fizz")
    else:
        print(numbers)
