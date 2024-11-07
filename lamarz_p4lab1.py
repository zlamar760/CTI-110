#Zachary LaMar
#11/5/24
#P4LAB1
#Use turtle to make shapes

import turtle
wn=turtle.Screen()
turt=turtle.Turtle()
turt.shape("turtle")

turt.pendown

turt.fillcolor("green")
turt.begin_fill()
for s in range (4):
    turt.forward(90)
    turt.right(90)
turt.end_fill()

turt.fillcolor("pink")
turt.begin_fill()
for t in range (3):
    turt.forward(90)
    turt.left(120)
turt.end_fill()


turt.penup()
turt.right(90)
turt.forward(120)
turt.left(90)
turt.forward(120)
turt.pendown()
turt.forward(70)
turt.right(135)
turt.forward(100)
turt.left(135)
turt.forward(70)

turt.penup()
turt.forward(20)
turt.left(90)
turt.pendown()
turt.forward(75)
turt.right(180)
turt.forward(75)
turt.left(90)
turt.forward(60)


turtle.exitonclick()
