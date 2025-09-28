import re

    
class StringCalculatorTDDKata:

    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter_part = parts[0][2:]
            
            if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
                delimiter = re.escape(re.findall(r'\[(.*?)\]', delimiter_part)[0])
            else:
                delimiter = re.escape(delimiter_part)
                
            numbers = parts[1]

        num_list = re.split(delimiter + "|,|\n", numbers)

        negatives = [int(n) for n in num_list if int(n) < 0]
        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
        
        num_list = [int(n) for n in num_list if int(n) <= 1000]
        return sum(num_list)
        
    