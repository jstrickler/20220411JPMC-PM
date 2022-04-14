from math import pi

def hello():
    print("Hello, JPMC world")

hello()

def circle_area(diameter):
    radius = diameter / 2
    area = pi * (radius ** 2)
    return area

x = hello()
a = circle_area(5)
print("x: {}".format(x))
print("a: {}".format(a))

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 8))

x = 100   # GLOBAL

def spam():
    y = 42  # LOCAL
    x = "guacamole"
    print("in spam: x is", x)
    print("in spam: y is", y)

def ham():
    y = "yam"
    print("in ham: y is", y)

spam()
ham()
print("in main: x is", x)
# print("in main: y is", y)

#  local -> nested -> global -> builtin



def foo():
    x = 5

    def bar():
        print("x")



print("\U0001F92F")


