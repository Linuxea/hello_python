# coding=utf-8

import turtle

i = 0

while True:
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
    fuc = 90 - i
    turtle.left(fuc)
    print(fuc)
    i += 1
    turtle.penup()
