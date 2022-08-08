# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()  # car = blueprint()
# print(timmy)  # Turtle object

# # object.function()
# timmy.shape("turtle")
# timmy.color("firebrick2")
# timmy.setx(100)

# my_screen = Screen()
# print(my_screen.canvheight)  # object.attribute
# my_screen.exitonclick()  # object.method()


# Turtle Graphics Doc: https://docs.python.org/3/library/turtle.html
# Turtle Color: https://cs111.wellesley.edu/labs/lab01/colors


from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon", "Type"]
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"],)
table.add_column("Type", ["Electric", "Water", "Fire"],)

table.align = "l"

print(table)