#unlimited arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1, 2, 3, 4, 5, 6, 7))

def calc(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(3, add=3, multiply = 10)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw["color"]

my_car = Car(make="Ford", color="blue", model="Ecosport")
print(my_car.model)

