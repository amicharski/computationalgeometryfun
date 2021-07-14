import geometry as Geometry
import tkinter as Tkinter
import math
import numpy as np
from random import randint


points = []
lines = []


def create_random_points():
    for i in range(1, 100):
        x = randint(5, width - 5)
        y = randint(5, height - 5)
        point = Geometry.Point(x, y)
        canvas.draw_point(point)
        points.append(point)


def detect_intersection(x1, y1, x2, y2, x3, y3, x4, y4): #no intersection = true, yes intersection = false
    # 1) Find the slope of the 2 lines
    slope1 = (y2 - y1)/(x2 - x1)
    if x4 != x3:
        slope2 = (y4 - y3) / (x4 - x3)
        # 2) Find the intersection point if one exists
        b1 = y1 - slope1 * x1
        b2 = y3 - slope2 * x3
        try:
            matrix = np.array([[slope1, slope2],
                               [1, 1]])
            aug = np.array([b1, b2])
            x = np.linalg.solve(matrix.T, aug)
        except np.linalg.LinAlgError as err:
            if "Singular matrix" in str(err): #a singular matrix is represented by two parallel lines
                return True
            else:
                print(err)
        # 3) If there is an intersection point, find out if it outside of the rectangle of the 4 points
        #a) sort the x and y coordinates
        x[0] = abs(x[0])
        x[1] = abs(x[1])
        xcoords = [x1, x2, x3, x4, x[0]]
        ycoords = [y1, y2, y3, y4, x[1]]
        #canvas.canvas.create_oval(x[0]-1, x[1]-1, x[0]+1, x[1]+1, tags="point", outline="red")
        xcoords.sort()
        ycoords.sort()
        #b) special case: if there are two x and y pairs that are the same
        counter = 0
        for i in xcoords:
            for j in ycoords:
                if i == j:
                    counter += 1
        if counter == 4:
            return True
        if xcoords[0] == x[0] or xcoords[4] == x[0]:
            if ycoords[0] == x[1] or ycoords[0] == x[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        #special case: vertical line detected, should work on this
        return False


def random_walk(x, y):
    for i in range(1, 6):
        x1 = width
        y1 = height
        while x+x1 < 0 or x+x1 > width or y+y1 < 0 or y+y1 > height or x1 == 0 or y1 == 0:
            x1 = randint(-90, 90)
            y1 = randint(-90, 90)
            if len(lines) > 0:
                for j in lines:
                    if not detect_intersection(j[0], j[1], j[2], j[3], x, y, x+x1, y+y1):
                        x1 = width
                        y1 = height
            #canvas.window.mainloop()
        lines.append([x, y, x + x1, y + y1])
        canvas.canvas.create_line(x, y, x + x1, y + y1, tags="randwalk")
        x += x1
        y += y1


def regen():
    canvas.delete("point")
    canvas.delete("randwalk")
    points.clear()
    lines.clear()
    random_walk(300, 300)
    #create_random_points()
    district.set(generate_district_name())


def generate_district_name():
    district_names = open("districtnames").readlines()
    size = len(district_names)
    line = randint(1, size+1)
    for p, l in enumerate(district_names):
        if p == line:
            return l


top = Tkinter.Tk()
top.title("Geometry")
top.resizable(0, 0)

height = 600
width = 600
top.geometry(str(height) + "x" + str(width))

district = Tkinter.StringVar()
district.set(generate_district_name())
name = Tkinter.Label(top, textvariable=district)
name.pack(side=Tkinter.TOP)

regen = Tkinter.Button(top, text="Regenerate", command=regen)
regen.pack(side=Tkinter.TOP)

canvas = Geometry.Canvas(top, height-50, width)
canvas.pack()
# have fun :)

random_walk(300, 300)
#create_random_points()

canvas.window.mainloop()
