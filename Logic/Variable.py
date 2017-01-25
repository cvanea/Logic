"""
Class for variable assignment in formulas.
"""


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

        :param tvalue: bool
        """
        self._tvalue = tvalue
