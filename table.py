from math_operations import Vector, Product, Val


class Table:
    # t = (
    #     (V0, V0, V0, V0, e1, V0, V0),
    #     (V0, V0, V0, V0, V0, e2, V0),
    #     (V0, V0, V0, V0, V0, V0, e3),
    #     (V0, V0, V0, V0, Product(a, e4), Product(b, e4), Product(c, e4)),
    #     (V0, V0, V0, V0, V0, V0, V0),
    #     (V0, V0, V0, V0, V0, V0, V0),
    #     (V0, V0, V0, V0, V0, V0, V0),
    # )
    def __init__(self, t):
        self.t = t

    def get(self, v1: Vector, v2: Vector):
        i = int(v1.symbol[1]) - 1
        j = int(v2.symbol[1]) - 1
        if i <= j:
            return self.t[i][j]
        else:
            return Product(Val(-1), self.t[j][i])
