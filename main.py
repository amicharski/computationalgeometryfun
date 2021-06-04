import tkinter as Tkinter
from random import randint

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="white", height=500, width=500)
def drawManyCircles(a):
    points = set()
    for i in range(0, a):
        x = randint(5, 495)
        y = randint(5, 495)
        coords = "(" + str(x) + ", " + str(y) + ")"
        points.add(coords)
        oval = C.create_oval(x - 5, y - 5, x + 5, y + 5)

drawManyCircles(5)
C.pack()
top.mainloop()