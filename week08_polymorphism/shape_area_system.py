class Figure:
    def compute_area(self):
        pass

class Box(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius * self.radius

class ThreeSide(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def compute_area(self):
        return 0.5 * self.base * self.height

shapes_list = [
    Box(10, 5),
    Round(5),
    ThreeSide(8, 6)
]

print("Box Area:", shapes_list[0].compute_area())
print("Round Area:", shapes_list[1].compute_area())
print("ThreeSide Area:", shapes_list[2].compute_area())