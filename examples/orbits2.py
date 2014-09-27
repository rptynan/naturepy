#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from naturepy.pvector import PVector
from naturepy.mover import Mover
import tkinter


C_HEIGHT = 512
C_WIDTH = 512
D_STEP = 10


def draw():
    global center, sat1, sat2

    f = sat2.grav_attract(sat1)
    sat1.apply_force(f)
    f = sat1.grav_attract(sat2)
    sat2.apply_force(f)

    sat1.check_edges(C_WIDTH, C_HEIGHT)
    sat1.update()
    sat1.display(canvas)
    sat2.check_edges(C_WIDTH, C_HEIGHT)
    sat2.update()
    sat2.display(canvas)

    canvas.after(D_STEP, draw)


root = tkinter.Tk()
root.title("Orbits")
canvas = tkinter.Canvas(root, height=C_HEIGHT, width=C_WIDTH)
canvas.pack(expand="YES")
canvas.configure(background="white")

sat1 = Mover(PVector(C_WIDTH/2, C_HEIGHT/3),
             PVector(0, 0), PVector(0, 0), 10)
sat1.vec.x = 1
sat2 = Mover(PVector(C_WIDTH/2, 2*(C_HEIGHT/3)),
             PVector(0, 0), PVector(0, 0), 10)
sat2.vec.x = -1

canvas.after(1, draw)
canvas.mainloop()
