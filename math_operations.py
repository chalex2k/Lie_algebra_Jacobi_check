from dataclasses import dataclass


class Scalar:
    pass


@dataclass
class Vector(Scalar):
    symbol: str

    def __str__(self):
        return self.symbol


@dataclass
class Coef(Scalar):
    symbol: str

    def __str__(self):
        return self.symbol


@dataclass
class Val(Scalar):
    val: float

    def __str__(self):
        return str(self.val)


class Expr:
    def calculate(self):
        return self


@dataclass
class Product(Expr):
    f1: Expr
    f2: Expr

    def calculate(self):
        if isinstance(self.f1, Expr):
            self.f1 = self.f1.calculate()
        if isinstance(self.f2, Expr):
            self.f2 = self.f2.calculate()
        return self

    # def __eq__(self, other):
    #     if not isinstance(other, Product):
    #         return False
    #     return self.f1 == other.f1 and self.f2 == other.f2 or\
    #            self.f1 == other.f2 and self.f2 == other.f1

    def __str__(self):
        return f'({str(self.f1)} * {str(self.f2)})'


@dataclass
class Sum(Expr):
    m1: Expr

    m2: Expr

    def calculate(self):
        if isinstance(self.m1, Expr):
            self.m1 = self.m1.calculate()
        if isinstance(self.m2, Expr):
            self.m2 = self.m2.calculate()
        return self

    def __str__(self):
        return f'({str(self.m1)} + {str(self.m2)})'


from constants import V0
# from table import Table

@dataclass
class Cross(Expr):
    """Векторное произведение"""
    table = None
    v1: Expr
    v2: Expr

    def calculate(self):
        if isinstance(self.v1, Vector) and isinstance(self.v2, Vector):
            if self.v1 == V0 or self.v2 == V0:
                return V0
            return self.table.get(self.v1, self.v2)
        elif isinstance(self.v1, Cross):
            self.v1 = self.v1.calculate()
            return self
        elif isinstance(self.v2, Cross):
            self.v2 = self.v2.calculate()
            return self
        elif isinstance(self.v1, Product):
            return Product(self.v1.f1, Cross(self.v1.f2, self.v2))  # TODO check on vector and coeff
        elif isinstance(self.v2, Product):
            return Product(self.v2.f1, Cross(self.v1, self.v2.f2))
        elif isinstance(self.v1, Sum):
            return Sum(Cross(self.v1.m1, self.v2), Cross(self.v1.m2, self.v2))
        elif isinstance(self.v2, Sum):
            return Sum(Cross(self.v1, self.v2.m1), Cross(self.v1, self.v2.m2))
        else:
            raise ValueError(f'invalid Cross {self.v1} {self.v2}')

    def __str__(self):
        return f'[{str(self.v1)}, {str(self.v2)}]'
