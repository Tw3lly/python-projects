# Easy mode lives 10
# Hard mode lives 5
# User should start by picking difficulty between easy and hard
# Program should pick a random number between 1 - 100
# Program should check if number is higher or lower or equal to guess
# If higher -> Warn user number is too high, lives goes down one point
# If lower -> Warn user number is too low, lives of guesses goes down one point
# If lives == 0, end game
# If equal to -> You got it! the answer was x, program exits

import random 
#from art import logo
# Choosing a random number and storing it in a variable
chosen_number = random.randint(1,100)

#print(logo)
print("Welcome to the numbers guessing game. \nI'm thinking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#Debug Print
#print(f"Chosen number: {chosen_number}")
# User sets difficulty, which will set the lives accordingly
if difficulty_choice == "easy":
  lives = 10
elif difficulty_choice == "hard":
  lives = 5
else:
  print("Please write easy or hard.")


# We want to be able to repeat guesses, so we make it a function. 
# We use return to return the value of the guess so we can use it outside the function. 
def make_a_guess():
  print(f"You have {lives} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  return guess

# Classic while loop, will run as long as game is not set to over. 
is_game_over = False
while not is_game_over:
  # Make guesses as long as game is not over
  guess = make_a_guess()
  #Debug print
  #print(guess)
  
  if guess == chosen_number:
    print(f"You got it! The answer was {guess}!")
    is_game_over = True
  
  elif guess > chosen_number:
    print(f"Too High! \nGuess again")
    lives -= 1
    if lives == 0:
      is_game_over = True
      print(f"You ran out of lives! The answer was {chosen_number}")
  
  elif guess < chosen_number:
    print("Too low! \n Guess again!") 
    lives -= 1 
    if lives == 0:
      print(f"You ran out of lives! The answer was {chosen_number}")
      is_game_over = True
  
  elif lives == 0:
    print(f"You ran out of lives! The answer was {chosen_number}")


#Debug Prints
#print(f" Lives: {lives}")
#print(f" Chosen number: {chosen_number}")
#print(f" Guessed number {guess}")
