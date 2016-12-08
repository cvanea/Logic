"""
Basic Classes for Formula Data Structure.
"""
from Logic.Expression import *


class Formula(object):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return str(self.formula)

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

    def convert_and_by_demorgans_law(self):
        return self.conversion_by_law(And, And.demorgan_law_and)

    def convert_not_by_double_negation(self):
        return self.conversion_by_law(Not, Not.double_negation)

    def convert_conditional_by_disjunction(self):
        return self.conversion_by_law(Conditional, Conditional.disjunction_convert)

    def convert_biconditional_by_conditional(self):
        return self.conversion_by_law(BiConditional, BiConditional.conditional_convert)
