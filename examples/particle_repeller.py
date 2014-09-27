#!/usr/bin/python3
import os
import sys
from random import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from naturepy.pvector import PVector
from naturepy.mover import Mover
from naturepy.particle import Particle
import tkinter


C_HEIGHT = 512
C_WIDTH = 512
D_STEP = 10


class ParticleSystem:

    def __init__(self, _origin):
        self.origin = _origin
        self.particles = []
        self.life_def = 125

    def run(self, canvas):
        self.particles[:] = [p for p in self.particles if not p.is_dead()]
        for p in self.particles:
            p.run(canvas)

    def add_particle(self):
        self.particles.append(Particle(self.origin, self.life_def))

    def apply_force(self, force):
        for p in self.particles:
            p.apply_force(force)


def draw():
    global ps, center

    for s in ps:
        for p in s.particles:
            if (p.loc - center.loc).magnitude() < 100:
                f = center.grav_attract(p)
                p.apply_force(f*-0.6)   # Repels
        s.apply_force(PVector(0, 0.05))
        s.run(canvas)
        s.add_particle()
        s.particles[len(s.particles)-1].vec = PVector(4*(random()-0.5),
                                                      4*(random()-0.5))

    canvas.after(D_STEP, draw)


root = tkinter.Tk()
root.title("Particle Shower")
canvas = tkinter.Canvas(root, height=C_HEIGHT, width=C_WIDTH)
canvas.pack(expand="YES")
canvas.configure(background="white")

center = Mover(PVector(C_WIDTH/2, C_HEIGHT/2),
               PVector(0, 0), PVector(0, 0), 20)
center.display(canvas)

ps = []
ps.append(ParticleSystem(PVector(C_WIDTH/5, C_HEIGHT/8)))
ps.append(ParticleSystem(PVector(2*(C_WIDTH/5), C_HEIGHT/8)))
ps.append(ParticleSystem(PVector(3*(C_WIDTH/5), C_HEIGHT/8)))
ps.append(ParticleSystem(PVector(4*(C_WIDTH/5), C_HEIGHT/8)))

canvas.after(1, draw)
canvas.mainloop()
