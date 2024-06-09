from turtle import Turtle


class LeftScore(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-120, 330)

    def print_score(self):
        self.write(arg=f"{self.left_score}", font=("Arial", 40, "normal"))

    def add_score(self):
        self.left_score = self.left_score + 1
        self.clear()


class RightScore(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(100, 330)

    def print_score(self):
        self.write(arg=f"{self.right_score}", font=("Arial", 40, "normal"))

    def add_score(self):
        self.right_score = self.right_score + 1
        self.clear()


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-70, 0)
        self.write(arg="GAME OVER", font=("Arial", 30, "normal"))
