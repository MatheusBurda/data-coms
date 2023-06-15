
# Convertion table

# 0000  000  0
# 0001  001  1
# 0010  002  2
# 0011  010  3
# 0100  011  4
# 0101  012  5
# 0110  020  6
# 0111  021  7
# 1000  022  8
# 1001  100  9
# 1010  101  10
# 1011  102  11
# 1100  110  12
# 1101  111  13
# 1110  112  14
# 1111  120  15


def encode(binary):
    ternary = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        decimal = int(byte, 2)
        ternary += convert_to_ternary(decimal)
    return ternary


def decode(ternary):
    binary = ""
    for i in range(0, len(ternary), 6):
        trit = ternary[i:i+6]
        decimal = convert_to_decimal(trit)
        binary += "{0:08b}".format(decimal)
    return binary


# \**********************************************\

def convert_to_ternary(decimal):
    ternary = ""
    while decimal > 0:
        remainder = decimal % 3
        ternary = str(remainder) + ternary
        decimal = decimal // 3
    return ternary.zfill(6)


def convert_to_decimal(trit):
    decimal = 0
    trit = trit[::-1]
    for i in range(len(trit)):
        decimal += int(trit[i]) * (3 ** i)
    return decimal


