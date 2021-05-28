from turtle import Turtle
import random

BALL_STEP = 6

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.movespeed =0
        self.xmove = BALL_STEP
        self.ymove = BALL_STEP
        self.speed("fastest")

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.xmove *= -1
        self.movespeed *= 0.7

    def y_bounce(self):
        self.ymove *= -1

    def reset(self):
        self.goto(0,0)
        self.movespeed = 0
        self.x_bounce()
