import re

    
class StringCalculatorTDDKata:

    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        parts = re.split(r',|\n', numbers)
        return sum(int(x) for x in parts)
        
    