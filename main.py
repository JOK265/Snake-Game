from turtle import Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()