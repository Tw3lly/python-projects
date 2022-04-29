# Imports
import turtle
import pandas

# Global Variables
ALIGNMENT = "center"
FONT = ('Courier', 12, "normal")

# Read files
data = pandas.read_csv("50_states.csv")

# Screen and background set-up.
screen = turtle.Screen()
screen.title("Guess the states")
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# Turtle that will write state names attributes
write_state_names = turtle.Turtle()
write_state_names.penup()
write_state_names.hideturtle()

# User score tracker and empty list where we can track already guessed answers
user_score = 0
user_previous_guesses = []
failed_states = []

# Game starts here
is_game_on = True
while is_game_on:
    # User input to guess state
    answer_state = screen.textinput(title=f"Score: {user_score}/50", prompt="Guess a state's name:").title()
    # If user exits the program, find out what states the user failed and save it to a CSV.
    if answer_state == "Exit":
        for s in data.state:
            if s not in user_previous_guesses:
                failed_states.append(s)
        df = pandas.DataFrame(failed_states)
        df.to_csv("Failed_states.csv")
        break
    # Loop through the states and check if they are equal to user guesses and not in the previously guessed list
    for states in data.state:
        if states == answer_state and answer_state not in user_previous_guesses:
            # Turtle needs to go to rows x and y coords from state guessed
            state_row = data[data.state == answer_state]
            state_x = int(state_row.x)
            state_y = int(state_row.y)
            write_state_names.goto(x=state_x, y=state_y)
            # Write the state name at coordinates above
            write_state_names.write(answer_state)
            # User Score will increase by one and append state to previously guessed states list
            user_previous_guesses.append(answer_state)
            user_score += 1

        # When user guesses reach 50, user has guessed all states and game will end
        elif user_score == 50:
            write_state_names.goto(0, 0)
            write_state_names.write(arg="Congratulations! You guessed them all!", align=ALIGNMENT, font=FONT)
            is_game_on = False

        # If answer is wrong or mistyped loop will repeat
        elif answer_state != states:
            pass
