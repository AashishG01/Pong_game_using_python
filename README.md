# Pong_game_using_python
The project involves creating a classic Pong game using Python's Turtle module. The game consists of two paddles and a ball. Players control the paddles to bounce the ball back and forth.

Setup:
Initialize the game window with turtle.Screen(), setting its title, background color, and dimensions. Disable automatic screen updates for smoother animations using win.tracer(0).

Game Objects:
Create two paddles using turtle.Turtle(), setting their shape to "square", color to white, and stretching their dimensions to form rectangles. Position the paddles on the left and right sides of the screen. Create the ball with turtle.Turtle(), setting its shape to "square" and color to white, and define its initial movement direction with ball.dx and ball.dy.

Movement:
Define functions to move the paddles up and down, binding these functions to keyboard keys (e.g., "w" and "s" for the left paddle, "Up" and "Down" for the right paddle).

Game Loop:
Update the screen continuously, moving the ball by updating its position based on ball.dx and ball.dy. Implement collision detection to reverse the ball's direction when it hits the top or bottom borders or collides with a paddle. Reset the ball's position and update scores when it goes past a paddle.

Scoring:
Maintain and display scores for both players using a turtle.Turtle() instance dedicated to the score display, updating it whenever a player scores.

This project demonstrates basic game development using Python's Turtle module, involving graphics, user input, and collision detection.
