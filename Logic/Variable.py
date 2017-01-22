"""
Class for variable assignment in formulas.
"""


class Variable(object):

    def __init__(self, variable):
        self.variable = variable
        self._tvalue = None

    def __str__(self):
        return str(self.variable)

    def __bool__(self):
        return self._tvalue

    @property
    def tvalue(self):
        return self._tvalue

    @tvalue.setter
    def tvalue(self, tvalue):
        self._tvalue = tvalue
