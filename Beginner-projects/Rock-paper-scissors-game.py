#import random will make sure that the 'random' module is present.
import random

# ASCII art representing rock, paper and scissors, tagged with variables so we can use them later. 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# User input, int function makes sure input gets stores as an integer
user_choice = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# Makes the choices into a list, so that the computer can choose a random one from this list
choices = [rock, paper, scissors]

#Computer will take from 'choices' list and choose one at random. We store the result in a variable.
computer_choice = random.choice(choices)

# Depending on the users choice we need to print out the corresponding ASCII art
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
# if user chooses an invalid number below will be printed
else:
  print("Please pick a valid number.")

# Prints out the computer choice as long as user typed a valid number
if user_choice >= 0 and user_choice < 3:
  print(f"Computer chose: \n {computer_choice}")

# Draw statements, maybe not the most readable or efficent way to solve this, but it works
if user_choice == 0 and computer_choice == rock:
  print("It's a draw.")
elif user_choice == 1 and computer_choice == paper:
  print("It's a draw.")
elif user_choice == 2 and computer_choice == scissors:
  print("It's a draw.")

# Win statements
if user_choice == 0 and computer_choice == scissors:
  print("You win!")
elif user_choice == 1 and computer_choice == rock:
  print("You win!")
elif user_choice == 2 and computer_choice == paper:
  print("You win!")

#Lose statements 
if user_choice == 0 and computer_choice == paper:
  print("You lose!")
elif user_choice == 1 and computer_choice == scissors:
  print("You lose!")
elif user_choice == 2 and computer_choice == rock:
  print("You lose!")

  # A more efficent solution: https://replit.com/@appbrewery/rock-paper-scissors-debugged-end 
