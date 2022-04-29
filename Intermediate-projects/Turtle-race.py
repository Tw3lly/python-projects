from turtle import Turtle, Screen
import random
# Keep the turtle colors in a list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False


screen = Screen()
# We add the perimeters to improve readability
screen.setup(width=500, height=400)
# User bet inputs
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# We save the y coordinates we start from and then modify it in the for loop 
# ,so that each turtle can get a new starting position
coordinates_y = -100
all_turtles = []

# Create turtle for loop, will loop 6 times
for t in range(6):
    # This is an example of multiple objects being created from the same class.
    new_turtle = Turtle(shape="turtle")
    # Color chosen for turtle based on how many times we have done the for loop
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=coordinates_y)
    coordinates_y += 30
    # We append all the new turtles to a list, so we can track them
    all_turtles.append(new_turtle)

# If user has made a bet, race will start 
if user_bet:
    is_race_on = True

while is_race_on:
    # For-loop loops through each turtle in all_turtles list
    for turtle in all_turtles:
        # If turtle x coordinates passed 230, that turtle wins and race ends.
        if turtle.xcor() > 230:
            is_race_on = False
            # We save the turtles pencolor to a variable, so we can print out which turtle won-
            # -and if the user bet on the right color
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        # While no turtle has passed finish line the turtle will choose a random pace from 0,10 to move forwards
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


