from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 4
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 340)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 40, "normal"))
        self.goto(200, 340)
        self.write(f"♡: {self.lives}", align="center", font=("Courier", 40, "normal"))

    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

    def take_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def final_score(self, outcome):
        self.goto(0, 0)
        if outcome == "win":
            self.write(f"Well done! Final score is: {self.score}", align="center", font=("Courier", 20, "normal"))
        elif outcome == "lose":
            self.write(f"You lose! Final score is: {self.score}", align="center", font=("Courier", 20, "normal"))