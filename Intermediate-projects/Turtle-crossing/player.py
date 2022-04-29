from turtle import Turtle
# Global Variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

# Create class and let in inherit from turtle module
class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Attributes of our turtle
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # Move speed, will move 10 paces at a time
    def move_up(self):
        self.forward(MOVE_DISTANCE)



