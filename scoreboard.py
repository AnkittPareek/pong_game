from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.goto(0, 260)
        self.hideturtle()

    def dashedline(self):
        posi=self.position()
        self.goto(0,240)
        self.color("white")
        self.pensize(4)
        self.setheading(270)
        while self.ycor() > -240:
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(30)

        self.penup()
        self.goto(posi)

