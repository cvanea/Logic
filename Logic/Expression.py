"""
Basic Classes for Expressions.
"""

from abc import abstractmethod


class Expression(object):

    def __init__(self, *scope):
        self.scope = scope

    def __str__(self, level=0):
        string = self.__class__.__name__ + "("
        l = len(self.scope) - 1
        for i, s in enumerate(self.scope):
            if i == l:
                string += str(s)
            else:
                string += str(s) + ", "
        string += ")"

        return string

    @abstractmethod
    def truth_value(self):
        pass

    @staticmethod
    def is_true(exp):
        try:
            return exp.truth_value
        except AttributeError:
            return exp


class UnaryExpression(Expression):
    def __init__(self, a):
        super().__init__(a)
        self.a = self.scope[0]

    @abstractmethod
    def truth_value(self):
        pass


class BinaryExpression(Expression):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = self.scope[0]
        self.b = self.scope[1]

    @abstractmethod
    def truth_value(self):
        pass


class Not(UnaryExpression):
    def __init__(self, a):
        super().__init__(a)

    @property
    def truth_value(self):
        return not self.is_true(self.a)

    @property
    def can_be_double_negated(self):
        if isinstance(self.a, Not):
            return True
        else:
            return False

    def double_negation(self):
        if isinstance(self.a, Not):
            return self.a.a
        else:
            return self  # going to need to deal with this


class Or(BinaryExpression):
    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def truth_value(self):
        if not self.is_true(self.a) and not self.is_true(self.b):
            return False
        else:
            return True

    def demorgans_law_or(self):
        return Not(And(Not(self.a), Not(self.b)))


class And(BinaryExpression):
    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def truth_value(self):
        if self.is_true(self.a) and self.is_true(self.b):
            return True
        else:
            return False

    def demorgan_law_and(self):
        return Not(Or(Not(self.a), Not(self.b)))


class Conditional(BinaryExpression):
    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def truth_value(self):
        if not self.is_true(self.a) or self.is_true(self.b):
            return True
        else:
            return False

    def disjunction_convert(self):
        return Or(Not(self.a), self.b)


class BiConditional(BinaryExpression):
    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def truth_value(self):
        if (self.is_true(self.a) and self.is_true(self.b)) or (
                not (self.is_true(self.a) or self.is_true(self.b))):
            return True
        else:
            return False

    def conditional_convert(self):
        return And(Conditional(self.a, self.b), Conditional(self.b, self.a))
