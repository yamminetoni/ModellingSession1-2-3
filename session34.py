from color_point import ColorPoint
from session12 import Point

class AdvancedPoint(ColorPoint):
    """
    Advanced Class showcasing interesting class concepts
    """
    COLORS = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        if color not in self.COLORS:
            raise TypeError(f"Color must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self): # property, getter
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value): # property, setter
        if value not in self.COLORS:
            raise TypeError(f"Color must be one of {self.COLORS}")
        self._color = value

    @classmethod
    def add_color(cls, color): # class method to add a new color
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_points(p1, p2): # this does not access any attributes!!
        return p1.distance_other(p2)

    @staticmethod
    def from_string(text):
        # i want to create an Advanced Point from a string: "red 2 7"
        # also called a "factory" method!
        color, x, y = text.split()
        if color not in AdvancedPoint.COLORS:
            raise TypeError(f"Color must be one of {AdvancedPoint.COLORS}")
        x = float(x)
        y = float(y)
        return AdvancedPoint(x, y, color)

AdvancedPoint.add_color("pink") # now pink is official
p2 = AdvancedPoint(4, 3, "pink")
print(p2)
# p2.x = 100
# print(p2)
p2.color = "yellow"
print(AdvancedPoint.COLORS) # proves that it is a class attribute
p1 = Point(0, 0)
print(AdvancedPoint.distance_2_points(p1, p2))
p2 = AdvancedPoint.from_string("pink 7 6.2") # calling the factory method!!
print(p2)