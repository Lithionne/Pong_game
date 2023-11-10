from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=4.5, stretch_len=0.85)
        self.penup()
        self.x = 350
        self.y = 0
        self.goto(self.x, self.y)
        self.color("white")
        self.up()
        self.down()

    def up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def down(self):
        self.y -= 20
        self.goto(self.x, self.y)


class PaddleLeft(Paddle):
    def __init__(self):
        super().__init__()
        self.x = -350
        self.goto(self.x, self.y)
        self.color("white")
