def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 6, 2))  # Tuple format


# KeyWordArguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.item():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]  # required kwargs
        self.model = kw["model"]
        self.color = kw.get("color")  # optional kwargs
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline", seats=2)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
