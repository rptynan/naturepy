#!/usr/bin/python3
import os
import sys
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from naturepy.pvector import PVector
from naturepy.mover import Mover
import tkinter


C_HEIGHT = 512
C_WIDTH = 512
D_STEP = 10


def on_mouse_move(event):
    mouse.loc.x, mouse.loc.y = event.x, event.y


def _sat_display(self):
    canvas.delete(self.canvas_id)
    self.canvas_id = canvas.create_circle(self.loc.x, self.loc.y,
                                          self.mass,
                                          outline="dark slate grey",
                                          width=1, fill="grey")
    canvas.delete(self.canvas_id2)
    # Swapping acc and vec here is interesting
    head = PVector(10 * math.cos(self.acc.heading()) + self.loc.x,
                   10 * math.sin(self.acc.heading()) + self.loc.y)
    self.canvas_id2 = canvas.create_circle(head.x, head.y,
                                           self.mass/2,
                                           outline="dark slate grey",
                                           width=1, fill="grey")


def draw():
    global mouse, sat
    # print(mouse.loc.x, mouse.loc.y)

    f = mouse.grav_attract(sat)
    sat.apply_force(f)

    sat.check_edges(C_WIDTH, C_HEIGHT)
    sat.display()
    sat.update()

    canvas.after(D_STEP, draw)


root = tkinter.Tk()
root.title("Mouse Attractor")
canvas = tkinter.Canvas(root, height=C_HEIGHT, width=C_WIDTH)
canvas.pack(expand="YES")
canvas.configure(background="white")

mouse = Mover(PVector(C_WIDTH/2, C_HEIGHT/2),
              PVector(0, 0), PVector(0, 0), 20)
Mover.display = _sat_display
sat = Mover(PVector(C_WIDTH/2, C_HEIGHT/2),
            PVector(0, 0), PVector(0, 0), 10)
sat.canvas_id2 = 0
sat.elast = -0.5

root.bind("<Motion>", on_mouse_move)
canvas.after(1, draw)
canvas.mainloop()
