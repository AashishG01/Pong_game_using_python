from turtle import Turtle, Screen
from ball import Ball
from paddle import PaddleLeft, PaddleRight
from scoreboard import LeftScore, RightScore, GameOver
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = PaddleLeft()
paddle_right = PaddleRight()
ball = Ball()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")


straight_line = Turtle()
straight_line.goto(0, 400)
straight_line.color("white")
straight_line.setheading(270)
straight_line.width(8)

for i in range(15):
    straight_line.forward(30)
    straight_line.penup()
    straight_line.forward(30)
    straight_line.pendown()

left_score = LeftScore()
left_score.print_score()

right_score = RightScore()
right_score.print_score()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    r_x = abs(paddle_right.x_coordinate() - ball.x_coordinate())
    r_y = abs(paddle_right.y_coordinate() - ball.y_coordinate())
    l_x = abs(paddle_left.x_coordinate() - ball.x_coordinate())
    l_y = abs(paddle_left.y_coordinate() - ball.y_coordinate())
    if (r_x < 15 and r_y < 25) or (l_x < 15 and l_y < 25):
        print("collision from paddle")
        # game_is_on = False
        # ball bouncing from the paddle
        if ball.angle() < 180:
            ball.go_to_angle(180 - ball.angle())
        elif ball.angle() > 180:
            ball.go_to_angle(540 - ball.angle())

        if ball.x_coordinate() > 0:
            right_score.add_score()
            right_score.print_score()
        elif ball.x_coordinate() < 0:
            left_score.add_score()
            left_score.print_score()
    # ball bouncing from the upper boundaries
    elif (380 < ball.y_coordinate() < 400 or
            -400 < ball.y_coordinate() < -380):
        print("collision from upper and lower boundaries")
        ball.go_to_angle(360 - ball.angle())

    elif ball.x_coordinate() > 400 or ball.x_coordinate() < -400:
        game_is_on = False
        game_over = GameOver()


screen.exitonclick()
