# List where we store all the letters of the alphabet twice, so the list can loop. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defines our caesar function
def caesar(text, shift, direction):
  # Empty variable where we will store the ciphered text
  cipher_text = ""
  # For each character in text that cannot be found in the alphabet, we will keep in the same position. 
  for char in text:
    if char not in alphabet:
      cipher_text += char
  # We will loop each letter in the text the user inputted. Each letter will get a new position depending on the shift setting and if the user chose to encode or decode. 
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift
    elif direction == "decode":
      new_position = position - shift
    cipher_text += alphabet[new_position]
  print(f"The {direction}d text is {cipher_text}")

#Imports and prints ASCII art logo.
import art 
print(art.logo)
# Variable which we use to check if program should continue running or not. If user does not want to continue loop, they will write 'no' and the value will be changed to 'False'
should_continue = True

# While loop checks variable above and will loop as long as that value is True. 
while should_continue == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  # If user inputs another statement other than encode or decode, while loop will break. 
  if direction != "encode" and direction != "decode":
    print("Please type encode or decode")
    break
  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # If the shift input is greater than 26 (the no of characters of the alphabet) we will use the modulo function to calculate which position that character would have if the alphabet would loop. EX 45 would be 19. 
  if shift > 26:
    shift = shift % 26
  # Run the caesar function
  caesar(text, shift, direction)

  # User input if they would like to run the program again. If no the should_continue will be changed to false and the while loop ends. 
  user_input = input("Do you want to go again? Type 'yes' to continue or 'no' to exit: \n").lower()
  if user_input == "no":
    should_continue = False
    print("Goodbye")
    
