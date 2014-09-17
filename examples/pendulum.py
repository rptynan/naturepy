#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from naturepy.pvector import PVector
from naturepy.mover import Mover
import tkinter
from math import pi, sin, cos


C_HEIGHT = 512
C_WIDTH = 512
D_STEP = 10
G_EARTH = 0.2


class Pendulum:

    def __init__(self, _pivot_loc, _bob):
        self.bob = _bob
        self.pivot_loc = _pivot_loc

        self.bob_id = 0
        self.line_id = 0
        self.pivot_id = 0

        self.damping = 0.9955
        self.angle = pi/4
        self.radius = 200
        self.a_vec = 0

    def display(self, canvas):
        canvas.delete(self.line_id)
        self.line_id = canvas.create_line(self.pivot_loc.x,
                                          self.pivot_loc.y,
                                          self.bob.loc.x, self.bob.loc.y,
                                          width=2)

        canvas.delete(self.pivot_id)
        self.pivot_id = canvas.create_circle(self.pivot_loc.x,
                                             self.pivot_loc.y,
                                             5, outline="black",
                                             width=1, fill="#6495ED")

        canvas.delete(self.bob_id)
        self.bob.loc = PVector(self.pivot_loc.x+sin(self.angle)*self.radius,
                               self.pivot_loc.y+cos(self.angle)*self.radius)
        self.bob_id = self.bob.display(canvas)

    def update(self):
        self.a_acc = (-1 * G_EARTH * sin(self.angle)) / self.radius
        self.a_vec += self.a_acc
        self.angle += self.a_vec
        self.a_vec *= self.damping


def draw():
    global pendulum

    pendulum.update()
    pendulum.display(canvas)

    canvas.after(D_STEP, draw)


root = tkinter.Tk()
root.title("Pendulum")
canvas = tkinter.Canvas(root, height=C_HEIGHT, width=C_WIDTH)
canvas.pack(expand="YES")
canvas.configure(background="white")

pendulum = Pendulum(PVector(C_WIDTH*0.5, C_HEIGHT*0.2),
                    Mover(PVector(0, 0), PVector(0, 0), PVector(0, 0), 20))

canvas.after(1, draw)
canvas.mainloop()
