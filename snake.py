from turtle import Turtle
POST=[(0,0),(-20,0),(-40,0)]
DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.snakelist=[]
        self.snakebuild()
        self.head=self.snakelist[0]

    def snakebuild(self):
        for i in POST:
            self.addsnake(i)
    #increasing the snake height
    def addsnake(self,snakepos):
        myt = Turtle(shape="square")
        myt.color("white")
        myt.penup()
        myt.goto(snakepos)
        self.snakelist.append(myt)
    def extend(self):
        self.addsnake(self.snakelist[-1].position())
        # print(self.snakelist[-1].position())

    def move(self):
        for snake in range(len(self.snakelist) - 1, 0, -1):
            # snake.penup()
            xc = self.snakelist[snake - 1].xcor()
            yc = self.snakelist[snake - 1].ycor()
            self.snakelist[snake].goto(x=xc, y=yc)
        self.head.forward(DIST)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != RIGHT:
            # self.snakelist[0].setheading(180)
            self.head.setheading(180)
    def up(self):
        if self.head.heading() != DOWN:
            # self.snakelist[0].setheading(90)
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            # self.snakelist[0].setheading(270)
            self.head.setheading(270)

