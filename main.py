from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from point import Point
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)

wall = Turtle()
wall.color("white")
wall.pensize(10)
wall.hideturtle()
wall.teleport(-300, 300)

for a in range(4):
    wall.forward(600)
    wall.right(90)

snake = Snake()

point = Point()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.2)    

    snake.move()



    # se a cobra pegar um ponto, cria um novo ponto na tela e aumenta o score
    if snake.head.distance(point) < 15:
        snake.extend()
        point.create_new_point()
        scoreboard.increase_score()

    # acaba o jogo quando a cobra colide com os limites da tela
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False
        
    # acaba o jogo quando a cobra colide com ela mesma
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

    if scoreboard.score > scoreboard.high_score:
        scoreboard.high_score = scoreboard.score
        scoreboard.update_high_score(scoreboard.high_score)



screen.exitonclick()