from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.tracer(n=0)
snake=Snake()
food=Food()
score=Score()
sc.listen()
sc.onkey(key="Right",fun=snake.right)
sc.onkey(key="Left",fun=snake.left)
sc.onkey(key="Up",fun=snake.up)
sc.onkey(key="Down",fun=snake.down)
gameon=True
while gameon:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        #to increase the snake height
        snake.extend()
        score.hit()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake .head.ycor()>280 or snake.head.ycor()<-280:
        gameon=False
        score.gameover()
    for i in range (1,len(snake.snakelist)):
        if snake.head.distance(snake.snakelist[i])<10:
            gameon=False
            score.gameover()
sc.exitonclick()