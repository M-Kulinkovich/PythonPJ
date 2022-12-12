class Rectangle:
    def __init__(self, w, h):
        self.h = h
        self.w = w

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


geom = [Rectangle(1, 2), Rectangle(2, 4), Square(10), Square(5)]

for g in geom:
    print(g.get_pr())
