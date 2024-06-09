from turtle import Turtle
import random
MOVE_DISTANCE = 20


class Ball:
    def __init__(self):
        self.bowl = Turtle()
        self.bowl.color("white")
        self.bowl.shape("circle")
        self.bowl.penup()
        self.bowl.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.bowl.setheading(random.randint(15, 45))
        # self.bowl.setheading(110)
        self.bowl.speed(7)

    def move(self):
        self.bowl.forward(MOVE_DISTANCE)

    def x_coordinate(self):
        return self.bowl.xcor()

    def y_coordinate(self):
        return self.bowl.ycor()

    def angle(self):
        return self.bowl.heading()

    def go_to_angle(self, new_angle):
        self.bowl.setheading(new_angle)
