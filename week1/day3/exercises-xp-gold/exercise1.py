import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is a closed shape where all points are equidistant "
              f"from a fixed center point (radius = {self.radius}).")

