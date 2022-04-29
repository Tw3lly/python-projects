from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen set-ups
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# Spawn the paddles, ball and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for keystrokes for both paddles
# R paddle uses up and down key, left uses W and S key
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# Game will loop as long as this variable stays True
game_is_on = True
while game_is_on:
    # We delay execution 0.1 as default, it will halve each time paddle hits ball,
    # which will make the ball looks like its moving faster
    # Screem will also update and then start moving the ball.
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detects collision with top or bottom wall, in that case it will bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detects collision with paddle, will bounce on impact
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # If right paddle misses, l will score a point and ball will reset position
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # If left paddle misses, r will score a point and ball will reset position
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    # If score is higher or equal to 10 on either side, that side will win and game is over
    if scoreboard.r_score >= 10:
        game_is_on = False
        scoreboard.r_wins_game_over()

    elif scoreboard.l_score >= 10:
        game_is_on = False
        scoreboard.l_wins_game_over()


screen.exitonclick()
