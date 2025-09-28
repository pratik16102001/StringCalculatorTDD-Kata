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

        negatives = [int(n) for n in num_list if int(n) < 0]
        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
        
        num_list = [int(n) for n in num_list if int(n) <= 1000]
        return sum(num_list)
        
    