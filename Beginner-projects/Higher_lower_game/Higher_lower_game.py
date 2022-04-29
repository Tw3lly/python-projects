# Imports
import random
from game_data import data
import art
from replit import clear

def choose_new_index():
  """Chooses an item from a random index in the data list"""
  new_index = random.randint(0,len(data) -1)
  return new_index

  # Saves our return from the choose_new_index function in a variable
compare_a = data[choose_new_index()]
compare_b = data[choose_new_index()]
while compare_a == compare_b:
  compare_b = data[choose_new_index()]

def compare_values(a, b, user):
  """Compares values and returns 1 if user guessed correctly, and 0 if they were wrong"""
  if a > b and user == "A":
    return 1
  elif a > b and user == "B":
    return 0
  elif b > a and user == "B":
    return 1
  else:
    return 0

is_game_over = False
user_score = 0

# While game is not over, the game will re-run. If user answers incorrectly, game will end. 
while not is_game_over:
  print(art.logo)
  # if user score is over 0, print the current score
  if user_score > 0:
    print(f"You're right, your current score is {user_score}")

  #Print Statements
  print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}" )
  print(art.vs)
  print(f"Against B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}" )
  
  #Debug print
  #print(f" Cheat: A = {compare_a['follower_count']} B = {compare_b['follower_count']} ")
  
  # User chooses value 
  user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

  #We have to compare the values
  answer = compare_values(a=compare_a['follower_count'],b=compare_b['follower_count'], user=user_choice)

  # if answer is equal to 1, the answer is correct
  if answer == 1:
    user_score += 1
    # We move the compare B item to compare A. 
    compare_a = compare_b
    compare_b = data[choose_new_index()]
    # A and B could be the same by chance, so while the values are the same, a new item will be picked
    while compare_a == compare_b:
      compare_b = data[choose_new_index()]
    clear()
  # if answer is equal to anything else, game will end and final score will be printed
  else:
    print(f"You were wrong! Your final score: {user_score}")
    is_game_over = True
  
  
# Lessons learned #
###################
# More efficent solution to choosing random item from list would just be to use random.choice, would make code cleaner
# def a function for the print statements that formats the data, would make code cleaner and readable
# Check answer by using if a_followers > b_followers
#                           return guess == "a"
#                       else: 
#                           return guess == "b"
#



