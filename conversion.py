
class Conversion:
    def __init__(self, c):
        self.c = c

    def c_f(self, c):
        f = round((c * 1.8) + 32, 2)
        return f

    def c_k(self, c):
        k = round(c + 273.15, 2)
        return k

    def c_r(self, c):
        r = round((c * 1.8) + 491.67, 2)
        return r
