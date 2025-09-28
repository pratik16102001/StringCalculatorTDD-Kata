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