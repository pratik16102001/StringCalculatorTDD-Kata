# String Calculator TDD Kata

A **Python String Calculator** developed **step-by-step using Test-Driven Development (TDD)**.

---

## Features

- Empty string → `0`  
- Single number → returns itself  
- Two or more numbers → sum  
- Newlines (`\n`) as separators  
- Custom single-character and multi-character delimiters  
- Multiple delimiters  
- Negative numbers → raises exception  
- Numbers > 1000 → ignored  

**Examples:**

```python
from calculator import StringCalculatorTDDKata

calc = StringCalculatorTDDKata()

calc.add("")                     # 0
calc.add("1")                    # 1
calc.add("1,2,3")                # 6
calc.add("1\n2,3")               # 6
calc.add("//;\n1;2")             # 3
calc.add("//[***]\n1***2***3")   # 6
calc.add("//[*][%]\n1*2%3")      # 6
