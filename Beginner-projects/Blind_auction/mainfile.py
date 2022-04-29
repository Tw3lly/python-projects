
# Imports, code was made in replit
from replit import clear
import art

# Prints logo art
print(art.logo)
# Creates empty dictionary called bids
bids = {}

# We define a function called make a bid so we can easily call it out later
def make_a_bid():
  name_input = input("What is your name? ")
  bid_input = input("What is your bid? $")
  # Adds inputs to dictionary, name will be key and bid will be value. We make sure the value gets input as an integer.
  bids[name_input] = int(bid_input)
  
  #Used for debug
  #print(bids)

# We create a variable that the while loop can check for to see if it should continue to run. 
continue_bids = True

#While value of continue_bids = True, the loop will run
while continue_bids == True:
  #Calls out function we made above
  make_a_bid()
  should_continue = input("Are there any more bidders? Type 'yes or 'no'.\n").lower()
  clear()
  #If user inputs no the loop will exit
  if should_continue == "no":
    continue_bids = False

# Empty variables
max_bid = 0
max_key = None

# Loops through each value in the dictionary. If value is higher than 0 or the previous numbers run it gets added to the variable we created above. 
for b in bids:
  if bids[b] > max_bid:
    max_bid = bids[b]
    max_key = b

#We print the result using an f string. 
print(f"The winner is {max_key} with a bid of ${max_bid}")

# Used for debug
#print(max_key)
#print(max_bid)

