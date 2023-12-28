from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            content = data.read()
            if content == "":
                self.high_score = 0
            else:
                self.high_score = int(content)
        self.hideturtle()
        self.update_scoreboard()

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(arg="Score: {} | High Score: {}".format(self.score, self.high_score),
                   move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
