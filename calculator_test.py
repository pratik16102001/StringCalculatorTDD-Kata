from calculator import StringCalculatorTDDKata


class TestStringCalculator:

    def setup_method(self):
        self.calc = StringCalculatorTDDKata()

    def test_empty_string_returns_zero(self):
        assert self.calc.add("") == 0