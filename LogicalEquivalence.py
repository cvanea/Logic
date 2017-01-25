from functools import reduce
from Logic.Expression import Not, And, Or, Conditional, BiConditional
from Logic.Formula import Formula


# def cartesian_product(n):
#     X = [(True, False) for i in range(n)]
#     return reduce(lambda acc, _X: [tup + (x,) for tup in acc for x in _X], X, [()])
#
#
# def main():
#     truth_cases = cartesian_product(1)
#
#     a_and_b = []
#     truth_table_a = []
#     truth_table_b = []
#
#     for i in truth_cases:
#         a = i[0]
#         # b = i[1]
#         # c = i[2]
#         a_and_b.append(i)
#         truth_table_a.append(Formula(a).truth_value)
#         truth_table_b.append(Formula(Not(Not(a))).convert_not_by_double_negation().truth_value)
#
#     for i, j in enumerate(a_and_b):
#         print(
#             "A: {0}  =>  {1} - {2}".format(str(j[0]), str(truth_table_a[i]), str(truth_table_b[i])))
#         # print(
#         #     "A: {0}, B: {1}, C: {2}  =>  {2} - {3}".format(str(j[0]), str(j[1]), str(j[2]), str(truth_table_a[i]),
#         #                                                    str(truth_table_b[i])))
#
#
# if __name__ == "__main__":
#     main()
