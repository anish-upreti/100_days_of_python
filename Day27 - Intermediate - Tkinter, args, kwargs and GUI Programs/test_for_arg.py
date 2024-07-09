def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(1, 2, 3, 4, 4))


def calculate(num, **kwargs):
    print(kwargs)

    print(kwargs["a"])
    num += kwargs["a"]
    num *= kwargs["b"]
    print(num)


calculate(4, a=4, b=5)


class Bike:
    def __init__(self, **kw):
        self.name = kw.get("name")
        self.color = kw.get("color")
        self.model = kw.get("model")


bike = Bike(name="Royal enfield", color="Black")
print(bike.name, bike.color)
print(bike.model)



