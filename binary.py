def string_to_binary(string):
    binario = ''
    for caractere in string:
        valor_ascii = ord(caractere)
        binario += format(valor_ascii, '08b')
    
    return binario


def binary_to_string(binario):
    string = ''
    substrings = [binario[i:i+8] for i in range(0, len(binario), 8)]
    
    for substring in substrings:
        valor_decimal = int(substring, 2)
        caractere = chr(valor_decimal)
        string += caractere
    
    return string