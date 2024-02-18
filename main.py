from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game number 2")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# top_paddle = Paddle((0, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
game_is_on = True
while game_is_on:
    time.sleep(ball.rychleji)
    screen.update()
    ball.move()

    # Detect collision ball with x wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("bounce")
        ball.bounce_x()

    # Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

