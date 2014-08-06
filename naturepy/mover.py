from .pvector import PVector
import naturepy.tk_monkey_patch
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

    def display(self, canvas):
        print(self.canvas_id)
        canvas.delete(self.canvas_id)
        self.canvas_id = canvas.create_circle(self.loc.x, self.loc.y,
                                              self.mass,
                                              outline="dark slate grey",
                                              width=1, fill="grey")

    def check_edges(self, width, height):
        if self.loc.x > width:
            self.loc.x = width
            self.vec.x *= -1
        if self.loc.x < 0:
            self.loc.x = 0
            self.vec.x *= -1
        if self.loc.y > height:
            self.loc.y = height
            self.vec.y *= -1
        if self.loc.y < 0:
            self.loc.y = 0
            self.vec.y *= -1

    def apply_force(self, force):
        self.acc += force / self.mass

    def grav_attract(self, m):
        force = self.loc - m.loc
        distance = force.magnitude()
        distance = max(5, distance)
        distance = min(25, distance)
        force.normalize()
        force *= (self.mass * m.mass) / (distance * distance)
        return force
