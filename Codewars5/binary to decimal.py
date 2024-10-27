# 1) Binary --> Decimal Conversion (2 ქულა)

# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15


def decimal(number):
    num = 0
    number = str(number)
    number = number[::-1]
    for i in range(len(number)):
        if number[i] == "1":
            num += 2 ** i
    return num


print(decimal(1001010101001))