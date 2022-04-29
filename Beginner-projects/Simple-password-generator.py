# We start by import random module and defining letters, numbers and symbols into lists
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print and user inputs, stores the user inputs as ints in a variable. 
print("Welcome to a simple Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# We create a str variable with nothing in it to store things later, we create one for each type of character.
letters1 = "" 
# For loops that repeats for the amount of letters/numbers/symbols the user chose. (if user chose 5, for loop repeats 5 times) and randomizes each character from the lists above. It then adds it into the empty variables we create. 
for i in range(nr_letters):
  letters1 += random.choice(letters)

numbers1 = ""
for i in range(nr_numbers):
  numbers1 += random.choice(numbers)

symbols1 = ""
for i in range(nr_symbols):
  symbols1 += random.choice(symbols)

# Combines the different characters to a string
final_password = letters1 + numbers1 + symbols1

# Not sure how to explain this one yet, but it takes the final_password string, uses the len function to seperate each character and then shuffles around those characters and prints the string after the characters have been randomized
print(''.join(random.sample(final_password,len(final_password))))


# Easy password solution, works if you don't care about randomizing the characters into different positions. The password will be in order of letters+numbers+symbols.
# print(f"{letters1}{numbers1}{symbols1}")
