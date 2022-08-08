# keyword ModuleName Keyword ModuleItem
from turtle import Turtle, Screen
import random

# from turtle import * (* = everything in module)
# from turtle as t (alias the import)

# Properties
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# # Challenge 1: Square
# turns = 4
# while turns != 0:
#     timmy.forward(100)
#     timmy.right(90)
#     turns -= 1


# # Challenge 2: Dashed Line
# pattern = 15
# while pattern != 0:
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     pattern -= 1


# # Challenge 3: Shapes
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# draw = True
# angles = 3
# while draw:
#     timmy.pencolor(random.choice(colors))
#     for corner in range(angles):
#         timmy.forward(100)
#         timmy.right(360/angles)
#
#     if angles == 10:
#         draw = False
#     else:
#         angles += 1


# # Challenge 4 & 5: Random Walk & Tuples
# directions = [0, 90, 180, 270]
# timmy.pensize(5)
# timmy.speed('fast')
#
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# # def random_color():
# #     timmy.pencolor(random.choice(colors))
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# def random_walk():
#     for steps in range(200):
#         timmy.pencolor(random_color())
#         timmy.forward(20)
#         timmy.setheading(random.choice(directions))
#
# random_walk()









screen = Screen()
screen.exitonclick()

