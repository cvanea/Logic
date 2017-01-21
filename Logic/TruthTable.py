"""
Class for truth tables and equivalence.
"""
from itertools import product as cartesian_product

from Logic.Formula import Formula
from Logic.Expression import Not


class TruthTable(object):

    def __init__(self, *formulas):
        self.formulas = formulas
        self._n = 2

    def number_of_variables(self, variables):
        _n = len(variables)
        return _n

    def __str__(self):
        paddings = []
        pass

    @property
    def _truth_values(self):
        return list(cartesian_product(*((True, False) for _ in range(self._n))))


def main():
    a = Formula(Not(Not(True)))
    b = Formula(Not(Not(Not(False))))
    x = TruthTable(a, b, a)
    print(x._truth_values)

if __name__ == '__main__':
    main()
