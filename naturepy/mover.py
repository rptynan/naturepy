#!/usr/bin/python3
from .pvector import PVector
import tkinter


class Mover:
    # Contains loc, vec, acc, mass
    canvas_id = 0

    def __init__(self, _loc, _vec, _acc, _mass):
        self.loc = _loc
        self.vec = _vec
        self.acc = _acc
        self.mass = _mass

    def update(self):
        self.vec += self.acc
        self.loc += self.vec
        self.acc *= 0

    def check_edges(self, width, height):
        if self.loc.x > width:
            self.loc.x = width
            self.vec.x *= -1
        if self.loc.x < 0 :
            self.loc.x = 0
            self.vec.x *= -1
        if self.loc.y > height:
            self.loc.y = height
            self.vec.y *= -1
        if self.loc.y < 0 :
            self.loc.y = 0
            self.vec.y *= -1


    def apply_force(self, force):
        self.acc += force / self.mass
