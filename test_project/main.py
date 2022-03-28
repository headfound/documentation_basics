from numbers import Number

test_var = 0

class Test_Class:
    """An example docstring for a class definition."""

    def __init__(self, test_var: Number):
        """Init method.

        :param test_var: Test parameter.
        :type test_var: Number
        """
        self.test_var = test_var

    def test_method(self, x: Number) -> Number:
        """Just a test Method.

        :param x: Test parameter
        :type x: Number
        :return: Two times the test parameter.
        :rtype: Number
        """
        return x * 2

def test_function(x: Number) -> Number:
    """Just a test function.

    :param x: Test parameter.
    :type x: Number
    :return: Three times the test paremater.
    :rtype: Number
    """
    return x * 3