import re

    
class StringCalculatorTDDKata:

    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        num_list = re.split(delimiter + "|,|\n", numbers)
        return sum(int(x) for x in num_list)
        
    