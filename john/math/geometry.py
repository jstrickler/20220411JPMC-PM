from math import pi


def hello():
    print("Hello, JPMC world")


def circle_area(diameter):
    radius = diameter / 2
    area = pi * (radius ** 2)
    return area


def rectangle_area(length, width):
    return length * width

# Dr. Evil voice:  "PRI-vate"
def _spam():
    print("spam spam spam")

