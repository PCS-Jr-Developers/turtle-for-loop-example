import turtle

# Sets up the turtle
turtle.speed(1)
turtle.color('red', 'yellow')
turtle.pensize(2)

# Draws a 36-ray star
turtle.begin_fill()
turtle.forward(200)  # Moves forward to start the star

# Draws the rays of the star
for _ in range(35):
    turtle.right(170)  # Turns the turtle
    turtle.forward(200)  # Draws the ray/point of a star

turtle.end_fill()

# Hides the turtle cursor and display the drawing
turtle.hideturtle()
turtle.done()