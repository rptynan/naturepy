import math


class PVector:
    # Contains x, y

    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def __add__(self, a):
        return PVector(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return PVector(self.x - a.x, self.y - a.y)

    def __mul__(self, scal):
        return PVector(self.x * scal, self.y * scal)

    def __truediv__(self, scal):
        try:
            return PVector(self.x / scal, self.y / scal)
        except ZeroDivisionError:
            return PVector(self.x, self.y)

    def magnitude(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def normalize(self):
        mag = self.magnitude()
        try:
            self.x /= mag
            self.y /= mag
        except ZeroDivisionError:
            pass
