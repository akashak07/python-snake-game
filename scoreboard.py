from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.upscore()
        self.hideturtle()
    def upscore(self):
        self.write(f"Your score:{self.score}", align="center", font=("Courier", 20, "normal"))
    def hit(self):
        self.score+=1
        self.clear()
        self.write(f"Your score:{self.score}", align="center", font=("Courier", 20, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!!", align="center", font=("Courier", 25, "normal"))

