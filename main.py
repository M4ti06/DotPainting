import colorgram
from turtle import Screen, Turtle
import random


colors = colorgram.extract("image.jpg", 30)
rgb_tuples = []


for color in range(len(colors)):
    r = colors[color].rgb[0]
    g = colors[color].rgb[1]
    b = colors[color].rgb[2]
    rgb_tuples.append((r, g, b))

colors_ready = [(202, 167, 134), (236, 243, 249), (144, 51, 99),
                (163, 167, 40), (237, 71, 121), (238, 83, 60), (17, 140, 64), (226, 117, 162), (239, 220, 72),
                (9, 141, 178), (67, 198, 218), (22, 171, 132), (158, 59, 53), (247, 231, 1), (111, 41, 86),
                (130, 187, 162), (31, 184, 199), (237, 163, 190), (244, 168, 156), (146, 217, 191), (139, 216, 224),
                (80, 36, 74), (128, 41, 35), (6, 111, 35), (187, 191, 216)]
tod = Turtle()
screen = Screen()
screen.colormode(255)
tod.speed("fastest")
tod.shape("circle")
tod.hideturtle()

tod.setheading(225)
tod.penup()
tod.forward(300)
tod.setheading(0)


dots_in_line = 0
for _ in range(10):
    for __ in range(10):
        tod.dot(20, random.choice(colors_ready))
        tod.penup()
        tod.forward(50)
        dots_in_line += 1
        if dots_in_line % 10 == 0 and dots_in_line > 0:
            tod.setheading(90)
            tod.forward(50)
            tod.setheading(180)
            tod.forward(500)
            tod.setheading(0)
            tod.pendown()


screen.exitonclick()