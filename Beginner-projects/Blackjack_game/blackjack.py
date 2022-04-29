#Imports
import random
from art import logo
from replit import clear

#Cards list with our cards, 11 is Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  """Will choose one random card from cards list and return that card. """
  card = random.choice(cards)
  return card

def calculate_initial_score(cards):
  """Calculates sum and checks if CPU or User has blackjack or gone over 21"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    # If ace is in CPU or Users hand and sum is over 21, value will be converted to 1 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    #Returns sum 0 if Blackjack, or the sum if no Blackjack spotted
  return sum(cards)

def compare(user_sum, cpu_sum):
  """Compares user_sum and cpu_sum, returns a string"""
  if user_sum > 21 and cpu_sum > 21:
    return "You are both over 21, you lose \n"

  if user_sum == cpu_sum:
    return "It's a draw! \n"

  elif cpu_sum == 0:
    return "You lost, House got Blackjack! \n"

  elif user_sum == 0:
    return "You win, you got Blackjack! \n"
  
  elif user_sum > 21:
    return "You got over 21, you lose!\n"
  
  elif cpu_sum > 21:
    return "House got over 21, you win! \n"
  
  elif user_sum > cpu_sum:
    return "You have the higher score, you win! \n"
  
  else:
    return "You lose, House wins! \n"


def play_game():
  # Prints logo at the start of each play_game
  print(logo)
  
  # Picks two card each for the user and CPU using choices() function
  user_pick = random.choices(cards, k=2)
  #user_sum = sum(user_pick)
  cpu_pick = random.choices(cards, k=2)
  #cpu_sum = sum(cpu_pick)
  
  #While game is not over we will continue 
  is_game_over = False
  while not is_game_over:
    # Calculate for blackjacks
    user_sum = calculate_initial_score(user_pick)
    cpu_sum = calculate_initial_score(cpu_pick)
    #print(f" Debug: {user_pick}, {cpu_pick}")
    #Prints current score and House first card.
    print(f"Your cards: {user_pick}, current score: {user_sum}")
    print(f"House first card: {cpu_pick[0]} \n ")
    
    # If user or cpu has a blackjack, the game is over
    if user_sum == 0 or cpu_sum == 0 or user_sum > 21:
      is_game_over = True
    else: 
      # if there is no blackjack game will continue and user will be prompted to choose if they want another card. 
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        # If user chooses another card, it will append the card returned from the deal_card() function
        user_pick.append(deal_card())
      else:
        # If uses answers no, game is over.
        is_game_over = True
  # While CPU sum is not a blackjack and sum is under 17, CPU will deal cards to itself
  while cpu_sum != 0 and cpu_sum < 17:
    cpu_pick.append(deal_card())
    cpu_sum = calculate_initial_score(cpu_pick)
  
  #When computer is done dealing to itself, results will be revealed. 
  print(f"   Your final hand: {user_pick}, final score: {user_sum}")
  print(f"   House final hand: {cpu_pick}, final score: {cpu_sum}")
  print(compare(user_sum, cpu_sum))

# We use a while function to be able to replay the game after last game is over.
# User will be prompted to choose, if choice is N program will exit. 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
