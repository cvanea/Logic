from Logic.Expression import Not, And, Or, Conditional, BiConditional
from Logic.Formula import Formula


def main():
    truth_values = [True, False]

    cart_prod = [(i, j) for i in truth_values for j in truth_values]

    for i in cart_prod:
        a = i[0]
        b = i[1]

        exp = Conditional(And(Not(Conditional(a, b)), Or(BiConditional(b, a), Not(Or(a, b)))), And(Or(a, b), a))

        formula = Formula(exp)

        print(formula.truth_value)


if __name__ == "__main__":
    main()
