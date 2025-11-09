from turtle import Turtle
from point import Point

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.teleport(position[0], position[1])
            self.segments.append(segment)


    def move(self):
        for a in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[a - 1].xcor()
            new_y = self.segments[a - 1].ycor()
            self.segments[a].teleport(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



    def left(self):
        "Altera o heading do objeto para o oeste"
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        "Altera o heading do objeto para o leste" 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        "Altera o heading do objeto para o norte" 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        "Altera o heading do objeto para o sul" 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    """if segments[0].distance(Point.point) < 15:
        Point.criar_novo_ponto()
        criar_novo_segmento(segments[-1].pos())


    # interrompe o jogo quando a cabeça da cobra alcança as bordas da tela
    if (segments[0].xcor() >= 300 or segments[0].xcor() <= -300 or 
        segments[0].ycor() >= 300 or segments[0].ycor() <= -300):
        game_is_on = False

    # interrompe o jogo quando a cabeça da cobra encosta em qualquer parte de seu corpo 
    for a in range(1, len(segments)):
        if segments[0].distance(segments[a]) < 10:
            game_is_on = False"""