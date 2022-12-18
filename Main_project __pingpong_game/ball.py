from turtle import Turtle,Screen

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.7)
        self.x=10
        self.y=10
        self.movespeed=0.1

    def move(self):
        newx=self.xcor()+self.x
        newy=self.ycor()+self.y
        self.goto(newx,newy)

    def bouncey(self):
        self.y*= -1
        
    def bouncex(self):
        self.x*= -1
        self.movespeed*=0.9

    def reset(self):
        self.goto(0,0)
        self.bouncex()
