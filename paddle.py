from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.sety(0)
        self.setheading(90)
        self.goto(position)

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)

