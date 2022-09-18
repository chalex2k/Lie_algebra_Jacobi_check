from copy import deepcopy
from itertools import combinations

from math_operations import Scalar, Cross, Sum
from constants import e1, e2, e3, e4, e5, e6, e7
from parser import parse_line
from simpl import sympy_simplify
from table import Table

t = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    t.append(list(map(parse_line, line.split(','))))


Cross.table = Table(t)


for i, j, k in combinations((e1, e2, e3, e4, e5, e6, e7), 3):
    print('------', i, j, k, '--------')
    f = Sum(Sum(Cross(Cross(i, j), k), Cross(Cross(k, i), j)), Cross(Cross(j, k), i))
    for _ in range(10):
        print(f)
        new_f = deepcopy(f).calculate()
        if isinstance(new_f, Scalar) or f == new_f:
            # print(new_f, f)
            f = new_f
            break
        f = new_f

    print(sympy_simplify(str(f)))
    print()
