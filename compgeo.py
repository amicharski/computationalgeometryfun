import time
import math
import tkinter as Tkinter
from random import randint


def key_pressed(event):
    if event.keycode == 13:
        generate()


def clear_canvas():
    for point in points:
        points.remove(point)
    for line in lines:
        lines.remove(line)
    C.delete("all")


def draw_many_circles(a):
    for i in range(1, a):
        x = randint(5, width - 5)
        y = randint(5, height - 5)
        coords = [str(x), str(y)]
        points.append(coords)
        #oval = C.create_oval(x - 5, y - 5, x + 5, y + 5)


def draw_many_lines(a):
    for i in range(1, a):
        point1 = points[randint(0, len(points) - 1)]
        points.remove(point1)
        point2 = points[randint(0, len(points) - 1)]
        #points.append(point1)
        points.remove(point2)
        C.create_line(point1[0], point1[1], point2[0], point2[1])


def connect_the_dots():
    subpoints = list()
    for i in points:
        subpoints.append(i)
        for j in subpoints:
            line = C.create_line(j[0], j[1], i[0], i[1])
            lines.append(line)  # add point #s to this


def sweep_line():
    for x in range(0, width):
        time.sleep(0.001)
        line = C.create_line(x, 0, x, height, fill='green')
        top.update()
        C.delete(line)


def generate():
    pts = 30
    clear_canvas()
    draw_many_circles(pts)
    #draw_many_lines(math.floor(pts/2))
    connect_the_dots()
    sweep_line()


if __name__ == "__main__":
    top = Tkinter.Tk()
    top.title("CompGeo")
    top.resizable(0, 0)
    height = 700
    width = 700
    top.geometry(str(height) + "x" + str(width))
    C = Tkinter.Canvas(top, bg="white", height=height, width=width)
    points = list()
    lines = list()
    top.bind("<Key>", key_pressed)
    C.pack()
    top.mainloop()