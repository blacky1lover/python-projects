import turtle

wn = turtle.Screen()
wn.bgcolor("red")  # set the window background color
turtle.shape("turtle")
tess = turtle.Turtle()
tess.color("blue")  # make tess blue
tess.pensize(3)  # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()
