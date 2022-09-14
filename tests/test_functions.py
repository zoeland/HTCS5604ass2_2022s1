import unittest
import string
import random

from functions import isAInt, isValidChoice, isValidInputNumber, isValidName, isValidPosition


def get_random_string(length):
    # Contain both lowercase and uppercase letters
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class TestFunctionMethods(unittest.TestCase):

    def test_isAInt(self):
        self.assertTrue(isAInt(0))
        self.assertTrue(isAInt('0'))
        self.assertTrue(isAInt(1000))
        self.assertFalse(isAInt(''))
        self.assertFalse(isAInt('X'))
        self.assertFalse(isAInt('1000X'))

    # Choice: "1" to "6"
    def test_isValidChoice(self):
        for i in range(1, 7):
            self.assertTrue(isValidChoice(str(i)))
        self.assertFalse(isValidChoice(0))
        self.assertFalse(isValidChoice("0"))
        self.assertFalse(isValidChoice("7"))

    # 0 < Name length <= 30
    def test_isValidName(self):
        self.assertTrue(isValidName(get_random_string(1)))
        self.assertTrue(isValidName(get_random_string(30)))
        self.assertFalse(isValidName(get_random_string(0)))
        self.assertFalse(isValidName(get_random_string(30) + '0'))

    # position in ["Guard", "Forward", "Centre"]
    def test_isValidPosition(self):
        self.assertTrue(isValidPosition('Guard'))
        self.assertTrue(isValidPosition('Forward'))
        self.assertTrue(isValidPosition('Centre'))
        self.assertFalse(isValidPosition('Center'))
        self.assertFalse(isValidPosition('XXXxxx'))

    def test_isValidInputNumber(self):
        self.assertTrue(isValidInputNumber(0, 0, 200))
        self.assertTrue(isValidInputNumber(199, 0, 200))
        self.assertTrue(isValidInputNumber(200, 0, 200))
        self.assertFalse(isValidInputNumber(-1, 0, 200))
        self.assertFalse(isValidInputNumber(201, 0, 200))


if __name__ == '__main__':
    unittest.main()
