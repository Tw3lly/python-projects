from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.goto(-220, 260)
        self.refresh_level()

    def refresh_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level} ", move=False, font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, font=FONT, align=ALIGNMENT)

