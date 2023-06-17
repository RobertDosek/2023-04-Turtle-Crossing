from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.color('black')
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)
