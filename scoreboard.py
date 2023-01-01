from turtle import Turtle
FONT= ("Courier", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_score()
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
    def add_score(self):
        self.score+=1
        self.write(f"Score:{self.score}", align="center", font=FONT)
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}", align="center", font=("Ariel", 15, "normal"))


