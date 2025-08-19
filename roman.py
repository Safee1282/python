class IntegerToRoman:
    def __init__(self, number):
        """Initialize with an integer number"""
        if not isinstance(number, int):
            raise TypeError("Value must be an integer")
        if number <= 0 or number > 3999:
            raise ValueError("Value must be between 1 and 3999")
        self.number = number

    def convert(self):
        """Convert the integer to Roman numeral"""
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        num = self.number
        roman = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += syms[i]
                num -= val[i]
            i += 1
        return roman


# Example usage
try:
    number = 3999
    converter = IntegerToRoman(number)
    print(f"Integer: {number} -> Roman Numeral: {converter.convert()}")
except (TypeError, ValueError) as e:
    print(e)