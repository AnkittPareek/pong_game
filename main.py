from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG by ANKIT")
screen.tracer(0)

right_paddle = Paddle((350, 0))
right_paddle.color("blue")
left_paddle = Paddle((-350, 0))
left_paddle.color("red")
ball = Ball()
score_l = ScoreBoard()
score_r = ScoreBoard()
dash = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="W", fun=left_paddle.move_up)
screen.onkey(key="S", fun=left_paddle.move_down)
dash.dashedline()
point_l = 0
point_r = 0
game_is_on = True

while game_is_on:
    # time.sleep(ball.movespeed)
    screen.update()

    ball.move()
    score_l.setx(-150)
    score_l.color("red")
    score_r.setx(+150)

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 \
            or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.x_bounce()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.y_bounce()

    if ball.xcor() > 390:
        point_l += 1
        ball.reset()
        score_l.clear()

    if ball.xcor() < -390:
        point_r += 1
        ball.reset()
        score_r.clear()

    score_l.write(f"Score : {point_l}", font=("Arial", 24,"normal"), align="center", )
    score_r.write(f"Score : {point_r}", font=("Arial", 24,"normal"), align="center", )

    if point_r == 7:
        winner = "Blue"
        game_is_on = False
    elif point_l == 7:
        winner = "Red"
        game_is_on = False

if game_is_on == False:
    dash.clear()
    dash.goto(0, 0)
    dash.pencolor("red")
    dash.write(f"Game Over!!!\n{winner} Wins.", font=("Arial", 30,"normal"), align="center")


screen.exitonclick()
