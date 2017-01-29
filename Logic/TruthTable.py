"""
Class for truth tables and equivalence.
"""
from itertools import product as cartesian_product

from Logic.Formula import Formula
from Logic.Expression import Not
from Logic.Variable import Variable


class TruthTable(object):

    def __init__(self, *formulas):
        self.formulas = formulas
        self.variables = {}
        for f in self.formulas:
            self.variables.update(f.variables)
        self._n = len(self.variables)



    def __str__(self):
        paddings = []
        pass

    @property
    def _truth_values(self):
        return list(cartesian_product(*((True, False) for _ in range(self._n))))


def main():

    a = Variable("a")
    b = Variable("b")

    f1 = Formula(Not(Not(a)))
    f2 = Formula(Not(Not(Not(b))))
    x = TruthTable(f1, f2)
    print(x._truth_values)

if __name__ == '__main__':
    main()
