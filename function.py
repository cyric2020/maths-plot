from math import sin


class Damp_Wave:
    def __init__(self, sin=0, A=1, b=1, c=1, d=0, f=0):
        self.sin = sin
        self.A = A
        self.b = b
        self.c = c
        self.d = d
        self.f = f

class Wave:
    def __init__(self, sin=0, A=1, b=1, c=0, d=0):
        self.sin = sin
        self.A = A
        self.b = b
        self.c = c
        self.d = d
