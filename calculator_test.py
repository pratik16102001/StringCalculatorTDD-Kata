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

        