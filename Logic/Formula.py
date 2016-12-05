"""
Basic Classes for Formula Data Structure.
"""
from Logic.Expression import *


class Formula(object):
    def __init__(self, formula):
        self.formula = formula

    @property
    def truth_value(self):
        return self.formula.truth_value

    def conversion_by_law(self, t, m):
        def f(x):
            if isinstance(x, t):
                return f(m.__call__(x))
            elif isinstance(x, UnaryExpression):
                return x.__class__(f(x.a))
            elif isinstance(x, BinaryExpression):
                return x.__class__(f(x.a), f(x.b))
            else:
                return x

        return Formula(f(self.formula))

    def convert_ors_by_demorgans_law(self):
        return self.conversion_by_law(Or, Or.demorgans_law_or)
