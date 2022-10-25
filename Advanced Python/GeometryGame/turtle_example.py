import turtle





if __name__ == "__main__":

    #creare una istance del canvas
    myturtle = turtle.Turtle()
    #non disegna le istruzioni successive
    myturtle.penup()
    #andare a certe coordinate
    myturtle.goto(200, -200)
    #disegna le istruzioni successive
    myturtle.pendown()
    myturtle.forward(100)
    myturtle.left(90)
    myturtle.forward(200)
    myturtle.left(90)
    myturtle.forward(100)
    myturtle.left(90)
    myturtle.forward(200)
    myturtle.dot(30, 'blue')

    turtle.done()