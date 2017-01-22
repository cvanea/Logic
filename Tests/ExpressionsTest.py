"""
Unit tests for the Expression classes.
"""
import unittest

from Logic import Not, Or, And, Conditional, BiConditional


class ExpressionTest(unittest.TestCase):

    #################
    # NOT
    #################

    def test_not(self):
        self.assertEqual(bool(Not(False)), True)
        self.assertEqual(bool(Not(True)), False)

    def test_not_conversion(self):
        self.assertEqual(
            bool(Not(True)),
            bool(Not(True).double_negation())
        )
        self.assertEqual(
            bool(Not(True)),
            bool(Not(Not(Not(True))).double_negation())
        )

    #################
    # OR
    #################

    def test_or(self):
        self.assertEqual(bool(Or(True, True)), True)
        self.assertEqual(bool(Or(True, False)), True)
        self.assertEqual(bool(Or(False, True)), True)
        self.assertEqual(bool(Or(False, False)), False)

    def test_or_conversion(self):
        self.assertEqual(
            bool(Or(True, True)),
            bool(Or(True, True).demorgans_law_or())
        )
        self.assertEqual(
            bool(Or(True, True)),
            bool(Not(And(Not(True), Not(True))))
        )

    #################
    # AND
    #################

    def test_and(self):
        self.assertEqual(bool(And(True, True)), True)
        self.assertEqual(bool(And(True, False)), False)
        self.assertEqual(bool(And(False, True)), False)
        self.assertEqual(bool(And(False, False)), False)

    def test_and_conversion(self):
        self.assertEqual(
            bool(And(True, True)),
            bool(And(True, True).demorgan_law_and())
        )
        self.assertEqual(
            bool(And(True, True)),
            bool(Not(Or(Not(True), Not(True))))
        )

    #################
    # CONDITIONAL
    #################

    def test_conditional(self):
        self.assertEqual(bool(Conditional(True, True)), True)
        self.assertEqual(bool(Conditional(True, False)), False)
        self.assertEqual(bool(Conditional(False, True)), True)
        self.assertEqual(bool(Conditional(False, False)), True)

    def test_conditional_conversion(self):
        self.assertEqual(
            bool(Conditional(True, True)),
            bool(Conditional(True, True).disjunction_convert())
        )
        self.assertEqual(
            bool(Conditional(True, True)),
            bool(Or(Not(True), True))
        )

    #################
    # BICONDITIONAL
    #################

    def test_biconditional(self):
        self.assertEqual(bool(BiConditional(True, True)), True)
        self.assertEqual(bool(BiConditional(True, False)), False)
        self.assertEqual(bool(BiConditional(False, True)), False)
        self.assertEqual(bool(BiConditional(False, False)), True)

    def test_biconditional_conversion(self):
        self.assertEqual(
            bool(BiConditional(True, True)),
            bool(BiConditional(True, True).conditional_convert())
        )
        self.assertEqual(
            bool(BiConditional(True, False)),
            bool(And(Conditional(True, False), Conditional(False, True)))
        )

if __name__ == '__main__':
    unittest.main()
