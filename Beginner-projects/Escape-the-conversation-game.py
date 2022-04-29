print('''
*******************************************************************************
  __     '                         ___
    ('__`>                           ./,  \            
    // o(                           //)< \\\       
    ':__/                          (/)\__)\`
     /_/\                          | \ )  (_
   |( ) \\ ,_                     __Y''(   \|
  [|\ `._-'\_(\\________________//_ `-./   /|
   ||`.___,-[______________________]-.___,'||
   \`\.,-) `-.|||               ||'   `-.,/||
    \,`.___.  |||              ,||  ,___,'_||
     |______`.|||             / ||,'_______||
        ||==I ||\            / ,|||||     |||
      __||__  ||_\__      __/_//|||||     |||
  ---o--o---o-||\_,-'----`-._// ||+||-----+||-------ool
*******************************************************************************
''')
print("Welcome to Escape The Conversation.")
print("Your mission is to escape the conversation.") 

#First choice input function. 
firstchoice = input('''You're at a party. You want to navigate the room but you are stuck in a conversation with someone you just met.\nYou don't want to be rude by abruptly ending the conversation. You have 2 choices. \n A) Ask a friend to rescue you \n B) Use your phone to fake an incoming call. \nWhat do you do? Type "A" or "B" ''')

# if statement that lowers the cases of the variable firstchoice, in case user either types in caps or without caps
if firstchoice.lower() == "a":
  
  #Program moves on to a second choice where we have two choices If statements works smimilarily as the first one.

  secondchoice = input('''You tried signaling a friend to save you, but your efforts failed.\nYou have 2 choices. \n A) Try to go and get some food. \n B) Try to find a natural transition in the conversation to end it. \nType "A" or "B". ''')
  if secondchoice.lower() == "b":

    # We now use the if and elif statements to be able to have 3 choices to choose from with 4 outcomes. If user types anyhing else than A,B,C a game over prompt will appear.
    thirdchoice = input("You tried to naturally transition the conversation but only got the other part more interested.\nYou are now desperate and have three options.\n A) You try to bring a third person in the conversation to escape.\n B) You try to leave things vague and just exit the conversation.\n C) Try to act sick to escape the conversation.")

    if thirdchoice.lower() == "b":
      print("Well done, turns out the easies option was the best option. You were able to escape the conversation gracefully.")

    elif thirdchoice.lower() == "a":
      print("You try to slowly walk away as a third person enters the conversation.\nThe third person brings you in the conversation again and you are now stuck in an even worse conversation. \n Game over.")

    elif thirdchoice.lower() == "c":
      print("Your desperate attempts are futile, the other person is looking at you in disgust as you desperately try to act sick to exit the conversation.\nYou fail miserably.\nGame over.")

    else:
      print("Game over!.")

#If user picks the wrong option or types something else entirely, Game Over prompt will appear by using the else function. . 
  else:
    print("There is no food at this party.\nYou look like a fool. \nGame over.")
else:
  print("The person you were talking to saw right through you and are now calling you a rude ahole behind your back.\nGame over. ")


