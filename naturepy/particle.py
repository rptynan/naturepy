from .pvector import PVector
import naturepy.tk_monkey_patch
import tkinter


class Particle:
    canvas_id = 0

    def __init__(self, _loc, _lifespan):
        self.loc = _loc
        self.vec = PVector(0,0)
        self.acc = PVector(0,0)
        self.org_lifespan = _lifespan
        self.lifespan = _lifespan

    def run(self, canvas):
        self.update()
        self.display(canvas)

    def update(self):
        self.vec += self.acc
        self.loc += self.vec
        self.acc *= 0
        self.lifespan -= 1

    def display(self, canvas):
        canvas.delete(self.canvas_id)
        try:
            ins = 255 - ((self.lifespan / self.org_lifespan) * 255)
        except ZeroDivisionError:
            ins = 0
        color = "#%02x%02x%02x" % (ins,ins,ins)
        self.canvas_id = canvas.create_circle(self.loc.x, self.loc.y,
                                              10, outline=color,
                                              width=1, fill=color)

    def is_dead(self):
        return self.lifespan <= 0

    def apply_force(self, force):
        self.acc += force / 1
