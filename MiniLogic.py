"""
Mini Propositional Logic for Master's Application.

Contains negation, disjunction, and conjunction as is sufficient for defining Propositional Logic.
For conditional and biconditional please see full library at https://github.com/cvanea/Logic .

Contains DeMorgan's Law for conjunction and disjunction, and Law of Double Negation.
Can check for tautological equivalence using '==' and truth value using '.truth_value()'.

"""

from abc import abstractmethod


class Expression(object):

    def __init__(self, *scope):
        """Init scope of any size.

        :param scope: Expression / Variable
        """
        self.scope = scope

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

        :param a: Expression / Variable
        """
        super().__init__(a)
        self.a = self.scope[0]

    @abstractmethod
    def __bool__(self):
        pass


class BinaryExpression(Expression):

    def __init__(self, a, b):
        """Init connectives with two scopes.

        :param a: Expression / Variable
        :param b: Expression / Variable
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

        :param a: Expression / Variable
        """
        super().__init__(a)

    def __bool__(self):
        """Define truth value.

        :return: Bool
        """
        return not self.a

    @property
    def can_be_double_negated(self):
        """Check for instance of double negation, e.g. Not(Not(a)).

        :return: Bool
        """
        return True if isinstance(self.a, Not) else False

    def double_negation(self):
        """Remove double negation.

        :return: Expression / Variable
        """
        return self.a.a if isinstance(self.a, Not) else self


class Or(BinaryExpression):

    def __init__(self, a, b):
        """Init disjunction connective object.

        :param a: Expression / Variable
        :param b: Expression / Variable
        """
        super().__init__(a, b)

    def __bool__(self):
        """Define truth value.

        :return: bool
        """
        return False if not self.a and not self.b else True

    def demorgans_law_or(self):
        """Apply DeMorgan's Law to a disjunction.

        :return: Expression
        """
        return Not(And(Not(self.a), Not(self.b)))


class And(BinaryExpression):

    def __init__(self, a, b):
        """Init conjunction connective object.

        :param a: Expression / Variable
        :param b: Expression / Variable
        """
        super().__init__(a, b)

    def __bool__(self):
        """Define truth value.

        :return: bool
        """
        return True if self.a and self.b else False

    def demorgan_law_and(self):
        """Apply DeMorgan's Law to a conjunction.

        :return: Expression
        """
        return Not(Or(Not(self.a), Not(self.b)))


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


class Variable(object):

    def __init__(self, variable):
        """Init variables to contain truth values.

        :param variable: String
        """
        self.variable = variable
        self._tvalue = None

    def __str__(self):
        """Return printable string for variable objects.

        :return: String
        """
        return str(self.variable)

    def __bool__(self):
        """Returns value of variable object.

        :return: Bool
        """
        return self._tvalue

    @property
    def tvalue(self):
        """Getter for truth value of variable object.

        :return: Bool
        """
        return self._tvalue

    @tvalue.setter
    def tvalue(self, tvalue):
        """Setter for truth value of variable object.

        :param tvalue: Bool
        """
        self._tvalue = tvalue


def main():
    """
    Script for showcasing various methods.

    """

    a = Variable("a")
    b = Variable("b")

    a.tvalue = True
    b.tvalue = False

    some_or = Formula(Or(Or(a, Or(a, b)), b))

    f1 = some_or.convert_ors_by_demorgans_law()
    f2 = f1.convert_not_by_double_negation()

    print(some_or)                  # >>> Or(Or(a, Or(a, b)), b)
    print(some_or.truth_value())    # >>> True
    print(f1)                       # >>> Not(And(Not(Not(And(Not(a), Not(Not(And(Not(a), Not(b))))))), Not(b)))
    print(f1.truth_value())         # >>> True
    print(f2)                       # >>> Not(And(And(Not(a), And(Not(a), Not(b))), Not(b)))
    print(f2.truth_value())         # >>> True
    print(some_or == f1)            # >>> True
    print(f1 == f2)                 # >>> True

if __name__ == "__main__":
    main()
