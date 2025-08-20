decimal_num = int(input("Enter a decimal number: "))

# Converting decimal to binary using bin() and slicing off the '0b'
binary_num = bin(decimal_num)[2:]

# Display result
print("Binary number:", binary_num)
