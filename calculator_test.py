import pytest
from calculator import StringCalculatorTDDKata


class TestStringCalculator:

    def setup_method(self):
        self.calc = StringCalculatorTDDKata()

    def test_empty_string_returns_zero(self):
        assert self.calc.add("") == 0

    def test_single_number_returns_itself(self):
        assert self.calc.add("1") == 1
        assert self.calc.add("3") == 3
        assert self.calc.add("5") == 5

    def test_two_numbers_comma_seprated_return_sum(self):
        assert self.calc.add("1,2") == 3
        assert self.calc.add("3,4") == 7
        assert self.calc.add("995, 995") == 1990

    def test_multiple_numbers_comma_separated_return_sum(self):
        assert self.calc.add("1,2,3,4") == 10
        assert self.calc.add("5,10,15") == 30
        assert self.calc.add("7,3,2,8,10") == 30

    def test_multiple_numbers_with_newline(self):
        assert self.calc.add("1\n2,3") == 6
        assert self.calc.add("4\n5\n6,7") == 22

    def test_custom_delimiter(self):
        assert self.calc.add("//;\n1;2") == 3
        assert self.calc.add("//|\n4|5|6") == 15

    def test_negative_numbers_raise_exception(self):
        with pytest.raises(Exception) as e:
            self.calc.add("-2,-5")
        assert str(e.value) == "Negatives not allowed: -2,-5"

        with pytest.raises(Exception) as e:
            self.calc.add("-5,-10")
        assert str(e.value) == "Negatives not allowed: -5,-10"

    def test_ignore_numbers_greater_than_1000(self):
        assert self.calc.add("2,1001") == 2