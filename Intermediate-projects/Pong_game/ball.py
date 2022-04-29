from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        """Moves ball to top right direction by increasing x-coords and y-coords by +10"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """When ball hits the top or bottom wall, y direction will change by *= -1"""
        self.y_move *= -1

    def bounce_x(self):
        """If ball bounces on paddle, x direction will change by *= -1, speed of ball will also increase"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """If any of the paddle misses, ball will reset to pos 0,0, reset speed and change direction of ball"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
