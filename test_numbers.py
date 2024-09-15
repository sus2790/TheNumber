import unittest

from the_number import isFinite, isInteger, isNumber


class TestIsNumber(unittest.TestCase):

    def test_isInteger(self) -> None:
        test_cases = [
            (1, True),
            (1.0, True),
            (1 + 2j, True),
            ("1", False),
            ([1], False),
            (None, False),
        ]
        for input_value, expected_output in test_cases:
            with self.subTest(input=input_value):
                assert isInteger(input_value) == expected_output

    def test_isFinite(self) -> None:
        inf = float("inf")
        nan = float("nan")
        test_cases = [
            (1, True),
            (1.0, True),
            (1 + 2j, True),
            (inf, False),
            (-inf, False),
            (nan, False),
            (1 + 1j * inf, False),
            (inf + 1j, False),
            ("1", False),
            (1 + 1j * nan, False),
            (nan + inf * 1j, False),
            (nan + nan * 1j, False),
        ]
        for input_value, expected_output in test_cases:
            with self.subTest(input=input_value):
                assert isFinite(input_value) == expected_output

    def test_isNumber(self) -> None:
        inf = float("inf")
        nan = float("nan")
        test_cases = [
            (1, True),
            (1.0, True),
            (-1.5, True),
            (1 + 2j, True),
            (inf, False),
            (-inf, False),
            (nan, False),
            ("1", False),
            (1 + 1j * inf, False),
            (1 + 1j * nan, False),
            (nan + inf * 1j, False),
            (nan + nan * 1j, False),
        ]
        for input_value, expected_output in test_cases:
            with self.subTest(input=input_value):
                assert isNumber(input_value) == expected_output


if __name__ == "__main__":
    unittest.main()
