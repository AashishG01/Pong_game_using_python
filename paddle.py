from turtle import Turtle


class PaddleLeft:
    def __init__(self):
        self.paddle_left = Turtle()
        self.paddle_left.color("white")
        self.paddle_left.shape("square")
        self.paddle_left.penup()
        self.paddle_left.setheading(90)
        self.paddle_left.goto(-350, 0)
        self.paddle_left.shapesize(stretch_wid=0.7, stretch_len=4)

    def move_up(self):
        self.paddle_left.forward(100)

    def move_down(self):
        self.paddle_left.backward(100)

    def x_coordinate(self):
        return self.paddle_left.xcor()

    def y_coordinate(self):
        return self.paddle_left.ycor()


class PaddleRight:

    def __init__(self):
        self.paddle_right = Turtle()
        self.paddle_right.color("white")
        self.paddle_right.shape("square")
        self.paddle_right.penup()
        self.paddle_right.setheading(90)
        self.paddle_right.goto(350, 0)
        self.paddle_right.shapesize(stretch_wid=0.7, stretch_len=4)

    def move_up(self):
        self.paddle_right.forward(100)

    def move_down(self):
        self.paddle_right.backward(100)

    def x_coordinate(self):
        return self.paddle_right.xcor()

    def y_coordinate(self):
        return self.paddle_right.ycor()
