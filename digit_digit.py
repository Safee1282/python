number = input("Enter a number: ")

# Remove negative sign if present
if number.startswith('-'):
    number = number[1:]

# Count digits
total_digits = len(number)

print("Total digits in the number:", total_digits)