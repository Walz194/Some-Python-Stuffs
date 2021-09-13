import turtle

turtle.shape('turtle')

turtle.setposition(-100, -100)
for i in range(0, 5):

    turtle.forward(100)
    turtle.right(110)
    turtle.forward(50)
    turtle.right(250)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

turtle.exitonclick()
