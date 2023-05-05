"""
module
"""


class Calculator:
    """class"""

    def __init__(self):
        """init"""
        self.result: int = 0

    def add(self, first_value: int, second_value: int):
        """
        calculate
        :return:
        """
        self.result = first_value + second_value
        return self.result

    def sub(self, first_value: int, second_value: int):
        """
        calculate
        :return:
        """
        self.result = first_value - second_value
        return self.result
