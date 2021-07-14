import math
import tkinter as Tkinter


class Canvas:
    # window            = tkinter window object
    # canvas            = canvas object
    # pack()            = basically self.canvas.pack()
    # delete(tags)      = basically self.canvas.delete(tags)

    def __init__(self, window, height, width):
        self.window = window
        self.canvas = Tkinter.Canvas(window, bg="white", height=height, width=width)

    def pack(self):
        self.canvas.pack(side=Tkinter.BOTTOM)

    def delete(self, tags):
        self.canvas.delete(tags)

    def draw_point(self, p):
        # p     = point

        self.canvas.create_oval(p.x-1, p.y-1, p.x+1, p.y+1, tags="point")

    def draw_vector(self, x, y, v):
        # x     = x starting point
        # y     = y starting point
        # v     = vector object

        self.canvas.create_line(x, y, x + v.x, y + v.y, arrow=Tkinter.LAST, tags="vector")


class Point:
    # x     = x-coordinate of the point
    # y     = y-coordinate of the point

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Vector:
    # x                         = x-coordinate of the vector
    # y                         = y-coordinate of the vector
    # magnitude                 = magnitude of the vector
    # angle                     = angle of the vector
    # add(v1, v2)               = adds two vectors
    # dot_product(*vectors)     = takes the dot product of 1 or more vectors
    # composition(u, v)         = composition of vector u onto v
    # projection(u, v)          = projection of vector u onto v

    def __init__(self, typ, arg1, arg2):
        if typ == "cartesian":
            self.x = arg1
            self.y = arg2
            self.magnitude = math.sqrt(arg1 ** 2 + arg2 ** 2)
            self.angle = math.acos(arg1 / self.magnitude)
        if typ == "polar":
            self.magnitude = arg1
            self.angle = arg2
            self.x = arg1 * math.cos(arg2)
            self.y = math.sqrt(arg1 ** 2 - self.x ** 2)

    @staticmethod
    def add(v1, v2):
        return Vector(v1.x + v1.y, v2.x + v2.y)

    @staticmethod
    def dot_product(*vectors):
        x_result = 1
        y_result = 1
        if len(vectors) < 1:
            raise Exception("Cannot take the dot product of 0 vectors")
        for v in vectors:
            x_result *= v.x
        for v in vectors:
            y_result *= v.y
        return x_result + y_result

    @staticmethod
    def composition(u, v): #composition of u onto v (comp v u)
        return Vector.dot_product(u, v)/v.magnitude

    @staticmethod
    def projection(u, v):   #projection of u onto v (proj v u)
        return Vector.dot_product(u, v)/v

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


if __name__ == "__main__":
    print("run this from a different file")
