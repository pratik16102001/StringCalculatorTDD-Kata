

    
class StringCalculatorTDDKata:

    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        if "," in numbers:
            parts = numbers.split(",")
            return sum(int(x) for x in parts)

        return int(numbers)
        
    