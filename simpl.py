import sympy as sp
from sympy import symbols


def sympy_simplify(expr: str):
    # a, b, c = symbols('a b c')
    # v0, e1, e2, e3, e4, e5, e6, e7 = symbols('v0, e1, e2, e3, e4, e5, e6, e7')
    return str(sp.sympify(expr)
)


if __name__ == '__main__':
    print(sympy_simplify('(v0 + (0 * (b * (c * e4))))'))
    print(sympy_simplify('(((1 + -1) * (b * (c * e4))) + v0)'))
