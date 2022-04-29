from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and then updates scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases left points by 1 and then calls update_scoreboard method"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases right points by 1 and then calls update_scoreboard method"""
        self.r_score += 1
        self.update_scoreboard()

    def l_wins_game_over(self):
        self.goto(0, 0)
        self.write(f"Game over! \nLeft side wins!", align="center", font=("Courier", 20, "normal"))

    def r_wins_game_over(self):
        self.goto(0, 0)
        self.write(f"Game over! \nRight side wins!", align="center", font=("Courier", 20, "normal"))
