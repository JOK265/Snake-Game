from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.teleport(0, 270)
        self.update_scoreboard()
        self.speed(1)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg= f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.pencolor("red")
        self.speed(1)
        self.hideturtle()
        self.write(arg= f"Game Over", move=False, align=ALIGNMENT, font=('Arial', 36, 'bold'))