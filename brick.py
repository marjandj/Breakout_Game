from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color, point):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.goto(position)
        self.point = point
        self.counter = 0

