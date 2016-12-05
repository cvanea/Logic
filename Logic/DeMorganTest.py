from Logic.Expression import Not, And, Or, Conditional, BiConditional
from Logic.Formula import Formula
from pprint import pprint


def main():

    a = True
    b = False

    some_or = Formula(Or(Or(Or(a, b), a), b))

    test = Not(Or(a, b))

    f = Formula(test)

    f2 = f.convert_ors_by_demorgans_law()

    f3 = some_or.convert_ors_by_demorgans_law()

    pprint(f2)

    pprint(f3)

    print(f2.truth_value == f.truth_value)

if __name__ == "__main__":
    main()

