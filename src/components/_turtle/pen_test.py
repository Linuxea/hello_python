# coding=utf-8

import turtle

i = 0
j = 0.1

while True:
    turtle.pendown()
    turtle.pensize(j)
    turtle.forward(10)
    turtle.left(45)
    turtle.penup()
    turtle.pendown()
    turtle.pensize(j)
    turtle.forward(10 + i)
    i += 1
    j += 0.1
