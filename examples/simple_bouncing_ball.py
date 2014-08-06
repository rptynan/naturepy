#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from naturepy.pvector import PVector
from naturepy.mover import Mover
import naturepy.tk_monkey_patch
import tkinter


C_HEIGHT = 320
C_WIDTH = 200
D_STEP = 5
G_EARTH = 9.8*(D_STEP/1000)


def draw():
    global circle

    f = gravity(circle)
    circle.apply_force(f)

    circle.check_edges(C_WIDTH, C_HEIGHT)
    if circle.loc.y == C_HEIGHT:
        circle.vec *= 0.8
    circle.update()

    canvas.delete(circle.canvas_id)
    circle.canvas_id = canvas.create_circle(circle.loc.x, circle.loc.y, 10,
                                            outline="dark slate grey",
                                            width=2, fill="grey")
    canvas.after(D_STEP, draw)


def gravity(m):
    return PVector(0, G_EARTH * m.mass)


root = tkinter.Tk()
root.title("Simple Bouncing Ball")
canvas = tkinter.Canvas(root, height=C_HEIGHT, width=C_WIDTH)
canvas.pack(expand="YES")
canvas.configure(background="white")

circle = Mover(PVector(C_WIDTH/2, C_HEIGHT/10),
               PVector(0, 0), PVector(0, 0), 10)
canvas.after(1, draw)
canvas.mainloop()
