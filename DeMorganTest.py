from Logic.Expression import Not, And, Or, Conditional, BiConditional
from Logic.Formula import Formula


def main():

    a = True
    # b = False

    # some_or = Formula(Or(Or(Or(a, b), a), b))

    some_not = Formula(Not(a))
    some_double_not = Formula(Not(Not(a)))
    some_triple_not = Formula(Not(Not(Not(a))))

    # f1 = some_or.convert_ors_by_demorgans_law()
    f2 = some_double_not.convert_not_by_double_negation()
    f3 = some_triple_not.convert_not_by_double_negation()
    #
    # # print(some_or)
    # # print(f1)
    #
    print(some_not)
    print(some_not.truth_value)

    print(some_double_not)
    print(some_double_not.truth_value)
    print(f2)

    print(some_triple_not)
    print(some_triple_not.truth_value)
    print(f3)
    print(f3 == some_triple_not)

if __name__ == "__main__":
    main()
