def __init__(self, x, y):
    """
    Initialize the class variables
    :param x: the x coordinate
    :param y: the y coordinate
    """
    self.x = x
    self.y = y


def __str__(self):
    """
    Return the string representation of the point
    :return: p<x, y>
    """
    return f"p<{self.x}, {self.y}>"


def __repr__(self):
    return self.__str__()


def distance_origin(self):
    """
    Return the distance from the origin to the point
    :return: float
    """
    return (self.x ** 2 + self.y ** 2) ** 0.5


def __lt__(self, other):
    """
    Compare two Points objects
    :param other: The other point object
    :return: bool True or False
    """


# instantiate the point class

p1 = Points(1, 2)
p2 = Points(3, 4)

print(p1.x, p1.y)
print(p1)

p3 = Points(4, 3)
print(p3.distance_origin())

p4 = Points(12, 5)
print(p4.distance_origin())

points = [p1, p2, p3, p4, Points(-2, 6)]
points.append(Points(-5, -5))

# x coordinate of the 5th point in the list
print(points[4].x)
print(points[5].distance_origin())

# print the entire lisst
print(points)
points.sort()
print(points)
points.append(7)
points.sort()
print(Point(x:7, y:11).distance_other(Point(x:7, y:15)))
