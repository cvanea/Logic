"""
Basic Classes for Formula Data Structure.
"""
from Logic.Expression import *


class Formula(object):

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return str(self.expression)

    def __bool__(self):
        return bool(self.expression)

    def __eq__(self, other, method='tvalue'):
        """Compare truth values by default.
        Set method to structure to compare the structure of two expression trees.
        :param other:
        :param method:
        :return:
        """
        if method == 'tvalue':
            return bool(self) == bool(other)
        elif method == 'structure':
            return self.__dict__ == other.__dict__

    def truth_value(self):
        return bool(self)

    def conversion_by_law(self, t, m):
        def f(x):
            if isinstance(x, t):
                return f(m.__call__(x))
            elif isinstance(x, Expression):
                return x.__class__(*(f(s) for s in x.scope))
            else:
                return x

        return Formula(f(self.expression))

    def convert_ors_by_demorgans_law(self):
        return self.conversion_by_law(Or, Or.demorgans_law_or)

    def convert_and_by_demorgans_law(self):
        return self.conversion_by_law(And, And.demorgan_law_and)

    def convert_conditional_by_disjunction(self):
        return self.conversion_by_law(Conditional, Conditional.disjunction_convert)

    def convert_biconditional_by_conditional(self):
        return self.conversion_by_law(BiConditional, BiConditional.conditional_convert)

    def convert_not_by_double_negation(self):
        def f(x):
            if isinstance(x, Not):
                if x.can_be_double_negated:
                    return f(x.double_negation())
                else:
                    return Not(f(x.a))
            elif isinstance(x, Expression):
                return x.__class__(*(f(s) for s in x.scope))
            else:
                return x

        return Formula(f(self.expression))
