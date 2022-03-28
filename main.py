
from numpy import number

test_var = 0

class Test_Class:
    def __init__(self, test_var):
        self.test_var = test_var

    def test_method(self, x: number) -> number:
        """Just a test Method.

        :param x: Test parameter
        :type x: number
        :return: Two times the test parameter.
        :rtype: number
        """
        return x * 2

def test_function(x: number) -> number:
    """Just a test function.

    :param x: Test parameter.
    :type x: number
    :return: Three times the test paremater.
    :rtype: number
    """
    return x * 3