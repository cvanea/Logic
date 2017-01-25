"""
Basic Classes for Formula Data Structure.
"""
from Logic.Expression import *


class Formula(object):

    def __init__(self, expression):
        """Init a formula object. Will always contain expressions.

        :param expression: Expression
        """
        self.expression = expression

    def __str__(self):
        """Call __str__ of expression.

        :return: String
        """
        return str(self.expression)

    def __bool__(self):
        """Call __bool__ of expression.

        :return: Bool
        """
        return bool(self.expression)

    def __eq__(self, other, method='tvalue'):
        """Compare truth values by default.

        Set method to structure to compare the structure of two expression trees.
        :param other: Formula
        :param method: Named parameter
        :return: Bool
        """
        if method == 'tvalue':
            return bool(self) == bool(other)
        elif method == 'structure':
            return self.__dict__ == other.__dict__

    def truth_value(self):
        """Call __bool__ of formula.

        :return: Bool
        """
        return bool(self)

    def conversion_by_law(self, t, m):
        """Recursively call respective conversion law on outer most expression.

        :param t: Expression
        :param m: Expression Class Method
        :return: Formula
        """
        def f(x):
            if isinstance(x, t):
                return f(m.__call__(x))
            elif isinstance(x, Expression):
                return x.__class__(*(f(s) for s in x.scope))
            else:
                return x

        return Formula(f(self.expression))

    def convert_ors_by_demorgans_law(self):
        """Calls conversion method for Or object.

        :return: Formula
        """
        return self.conversion_by_law(Or, Or.demorgans_law_or)

    def convert_and_by_demorgans_law(self):
        """Calls conversion method for And object.

        :return: Formula
        """
        return self.conversion_by_law(And, And.demorgan_law_and)

    def convert_conditional_by_disjunction(self):
        """Calls conversion method for Conditional object.

        :return: Formula
        """
        return self.conversion_by_law(Conditional, Conditional.disjunction_convert)

    def convert_biconditional_by_conditional(self):
        """Calls conversion method for Biconditional object.

        :return: Formula
        """
        return self.conversion_by_law(BiConditional, BiConditional.conditional_convert)

    def convert_not_by_double_negation(self):
        """Check for double negation and recursively apply method to expression.

        :return: Formula
        """
        def f(x):
            if isinstance(x, Not):
                return f(x.double_negation()) if x.can_be_double_negated else Not(f(x.a))
            elif isinstance(x, Expression):
                return x.__class__(*(f(s) for s in x.scope))
            else:
                return x

        return Formula(f(self.expression))
