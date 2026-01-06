from turtle import Screen
from time import sleep
from snake import Snake
from point import Point
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)

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
    sleep(0.1)    

    snake.move()

    snake_head_position = snake.segments[0].pos()

    if snake.head.distance(point) < 15:
        point.create_new_point()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()