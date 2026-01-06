from turtle import Turtle
from random import randint

class Point(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5)
        self.create_new_point()

    
    def create_new_point(self):
        point_x = round(randint(-280, 280) / 20) * 20
        point_y = round(randint(-280, 280) / 20) * 20
        self.teleport(point_x, point_y)
