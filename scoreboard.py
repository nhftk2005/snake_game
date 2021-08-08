from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            return int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.get_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


