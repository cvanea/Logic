"""
Basic Classes for Expressions. Contains all Propositional Logic connectives.
"""

from abc import abstractmethod


class Expression(object):

    def __init__(self, *scope):
        """Init scope of any size.

        :param scope: Expression - Scope of Connective
        """
        self.scope = scope
        self.variables = {}

    def __str__(self):
        """Return printable expression as a string.

        :return: String
        """
        string = self.__class__.__name__ + "("
        l = len(self.scope) - 1
        for i, s in enumerate(self.scope):
            if i < l:
                string += str(s) + ", "
            else:
                string += str(s)
        string += ")"

        return string

    @abstractmethod
    def __bool__(self):
        pass


class UnaryExpression(Expression):

    def __init__(self, a):
        """Init connectives with one scope.

        :param a: Scope
        """
        super().__init__(a)
        self.a = self.scope[0]

    @abstractmethod
    def __bool__(self):
        pass


class BinaryExpression(Expression):

    def __init__(self, a, b):
        """Init connectives with two scopes.

        :param a: Expression - Left most scope
        :param b: Expression - Right most scope
        """
        super().__init__(a, b)
        self.a = self.scope[0]
        self.b = self.scope[1]

    @abstractmethod
    def __bool__(self):
        pass


class Not(UnaryExpression):

    def __init__(self, a):
        """Init negation connective object.

        :param a: Expression - Scope
        """
        super().__init__(a)

    def __bool__(self):
        return not self.a

    @property
    def can_be_double_negated(self):
        """Check for instance of double negation, e.g. Not(Not(a)).

        :return: Bool
        """
        if isinstance(self.a, Not):
            return True
        else:
            return False

    def double_negation(self):
        """Remove double negation.

        :return: Expression - Scope of scope
        """
        if isinstance(self.a, Not):
            return self.a.a
        else:
            return self


class Or(BinaryExpression):

    def __init__(self, a, b):
        """Init disjunction connective.

        :param a: Left most scope
        :param b: Right most scope
        """
        super().__init__(a, b)

    def __bool__(self):
        return False if not self.a and not self.b else True

    def demorgans_law_or(self):
        """Apply DeMorgan's Law to a disjunction.

        :return: Formula
        """
        return Not(And(Not(self.a), Not(self.b)))


class And(BinaryExpression):

    def __init__(self, a, b):
        """Init conjunction connective.

        :param a: Left most scope
        :param b: Right most scope
        """
        super().__init__(a, b)

    def __bool__(self):
        return True if self.a and self.b else False

    def demorgan_law_and(self):
        """Apply DeMorgan's Law to a conjunction.

        :return: Formula
        """
        return Not(Or(Not(self.a), Not(self.b)))


class Conditional(BinaryExpression):

    def __init__(self, a, b):
        """Init conditional connective.

        :param a: Antecedent scope
        :param b: Consequent scope
        """
        super().__init__(a, b)

    def __bool__(self):
        return True if not self.a or self.b else False

    def disjunction_convert(self):
        """Apply disjunction conversion to conditional.

        :return: Formula
        """
        return Or(Not(self.a), self.b)


class BiConditional(BinaryExpression):

    def __init__(self, a, b):
        """Init bi-conditional connective.

        :param a: Left most scope
        :param b: Right most scope
        """
        super().__init__(a, b)

    def __bool__(self):
        return True if (self.a and self.b) or not (self.a or self.b) else False

    def conditional_convert(self):
        """Apply conversion to conditionals.

        :return: Formula
        """
        return And(Conditional(self.a, self.b), Conditional(self.b, self.a))
