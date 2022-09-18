import re
from typing import List

from math_operations import Val, Coef, Vector, Sum, Product


def parse_line(line: str):
    """Разбирает строковое выражение на объекты из math_operations.py"""
    s = re.split('( |\*|\+|\n)', line)
    s = list(filter(lambda x: x not in ('', ' ', '\n'), s))
    return _parse(s)


def _parse(expr: List[str]):
    if len(expr) == 1:
        try:
            return Val(int(expr[0]))
        except ValueError:
            if expr[0] in ('a', 'b', 'c'):
                return Coef(expr[0])
            elif expr[0] in ('e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'v0'):
                return Vector(expr[0])
            raise ValueError(expr[0])
    else:
        for i, s in enumerate(expr):
            if s == '+':
                return Sum(_parse(expr[:i]), _parse(expr[i + 1:]))
        for i, s in enumerate(expr):
            if s == '*':
                return Product(_parse(expr[:i]), _parse(expr[i + 1:]))
    return ValueError(expr)


if __name__ == '__main__':
    for s in (
        'a + b',
        'e1 + 2*e2',
        '0 * e1 - 2*e2',
        '0*e1+-2+e2',
        '0',
        'v0'
    ):
        parsed = parse_line(s)
        print(s, ':', parsed, type(parsed))
