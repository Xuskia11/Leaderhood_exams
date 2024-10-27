# 2) Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111


def binary(number):
    bin = ""
    while number > 0:
        num = number % 2
        bin = bin + str(num)
        number //= 2

    return int(bin) 

print(binary(123))