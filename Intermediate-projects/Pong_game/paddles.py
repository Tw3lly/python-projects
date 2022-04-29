from turtle import Turtle


# Spawn class and let it inherit from turtle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    # defines the control settings, paddle will take current y coords and them in order to move
    def up(self):
        """Will tell paddle to move up, y-coords changes by +20 on each key press."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Will tell paddle to move down, y-coords changes by -20 on each key press."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
