from Logic import Not, And, Or, Conditional, BiConditional
from Logic import Formula
from Logic import Variable


def main():

    a = Variable("a")
    b = Variable("b")

    a.tvalue = True
    b.tvalue = False

    some_or = Formula(Or(Or(a, Or(a, b)), b))

    x = some_or.convert_ors_by_demorgans_law()
    y = x.convert_not_by_double_negation()
    print(x)
    print(y)
    print(x == y)
    print(x.truth_value())

    # print(some_or)
    # print(some_not)
    #
    # print(some_or.truth_value())
    # print(some_not.truth_value())
    #
    # print(Not(a).double_negation())


if __name__ == "__main__":
    main()
