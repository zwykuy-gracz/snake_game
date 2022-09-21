from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def end_of_game(self):
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write(f"You lost! your score was: {self.score}", move=False, align=ALIGNMENT, font=FONT)