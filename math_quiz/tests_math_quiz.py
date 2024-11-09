import unittest
from math_quiz import RandomInt, RandomOp, Calculation


class TestMathGame(unittest.TestCase):

    def test_RandomInt(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomOp(self):
        # TODO
        pass

    def test_Calculation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 3, '+', '5 + 3', 8),
            (5, 4, '+', '5 + 4', 9),
            (5, 5, '+', '5 + 5', 10),
            (5, 6, '+', '5 + 6', 11),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # TODO
            pass


if __name__ == "__main__":
    unittest.main()
