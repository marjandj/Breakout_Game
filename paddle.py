from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -300)

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())
