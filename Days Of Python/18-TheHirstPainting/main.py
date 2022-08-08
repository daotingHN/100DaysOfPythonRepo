# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('damien-hirst-lactulose.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176),
                  (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
                  (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86),
                  (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161),
                  (152, 213, 190), (242, 205, 8), (89, 48, 31)]
    color = random.choice(color_list)
    return color


def paint_row():
    for x in range(10):
        timmy.color(random_color())
        timmy.dot(20)
        timmy.forward(50)


def next_row(row):
    timmy.goto(-230, ((-275) + (50 * row)))


def paint_hirst():
    timmy.penup()
    timmy.speed("fastest")
    row = 1

    while row != 11:
        next_row(row)
        paint_row()
        row += 1

    timmy.goto(0, 0)


paint_hirst()

screen = turtle.Screen()
screen.exitonclick()