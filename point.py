from turtle import Turtle
from random import randint

class Point:

    def __init__(self):
        self.criar_novo_ponto()

    point = Turtle('circle')
    point.color('red')
    point.shapesize(0.5)

    def criar_novo_ponto(self):
        point_x = round(randint(-280, 280) / 20) * 20
        point_y = round(randint(-280, 280) / 20) * 20
        self.teleport(point_x, point_y)

    criar_novo_ponto(point)