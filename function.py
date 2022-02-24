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

class Exponential:
    def __init__(self, A=1, b=1, c=0):
        self.A = A
        self.b = b
        self.c = c

class Linear_Bounce:
    def __init__(self, BugA_X, BugA_Y, BugB_X, BugB_Y, n, m):
        self.BugA_X = BugA_X
        self.BugA_Y = BugA_Y
        self.BugB_X = BugB_X
        self.BugB_Y = BugB_Y
        self.n = n
        self.m = m