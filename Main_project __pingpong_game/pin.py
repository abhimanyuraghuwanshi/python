from turtle import Turtle,Screen, screensize
from paddle import tim
from ball import ball
from score import scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(600,400)
screen.tracer(0)

rtim=tim((280,0))
ltim=tim((-280,0))
ball=ball()
score=scoreboard()

screen.listen()
screen.onkey(rtim.up,"Up")
screen.onkey(rtim.down,"Down")
screen.onkey(ltim.up,"a")
screen.onkey(ltim.down,"s")

gameon=True
while gameon:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>185 or ball.ycor()<-185:
       ball.bouncey()
    if ball.distance(rtim)<30 and ball.xcor()<290 or ball.distance(ltim)<30 and ball.xcor()>-290:
       ball.bouncex()

    if ball.xcor()>300:
        ball.reset()
        score.lpoint()
    if ball.xcor()<-300:
        ball.reset()
        score.rpoint()

screen.exitonclick()