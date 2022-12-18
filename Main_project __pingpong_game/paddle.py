from turtle import Turtle,Screen, screensize
class tim(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(3,0.5)
        self.penup()
        self.goto(position)

    def up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(),newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(),newy)