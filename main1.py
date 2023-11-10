from turtle import Screen
from paddle_1 import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

pad_right = Paddle((350, 0))
pad_left = Paddle((-350, 0))

screen.onkey(key="Up", fun=pad_right.up)
screen.onkey(key="Down", fun=pad_right.down)
screen.onkey(key="w", fun=pad_left.up)
screen.onkey(key="s", fun=pad_left.down)

ball = Ball()

scoreboard = ScoreBoard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad_right) < 50 and ball.xcor() > 325:
        # ball.speed_right()
        ball.bounce_x()
    elif ball.distance(pad_left) < 50 and ball.xcor() < -325:
        # ball.speed_left()
        ball.bounce_x()

    if ball.xcor() >= 380:
        ball.reset()
        scoreboard.ad_point_left()

    elif ball.xcor() <= -380:
        ball.reset()
        scoreboard.ad_point_right()

screen.exitonclick()
