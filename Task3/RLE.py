# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from unittest import result

def RLE_Encode(data):
    res = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                res += str(count) + prev_char
            count = 1
            prev_char = char
        else: 
            count+=1
    else:
        res += str(count) + prev_char
        return res

def RLE_Decode(encode_value):
    decode = ''
    count = ''
    for char in encode_value:
        if char.isdigit():
            count += char
        else:
            decode += char*int(count)
            count = ''
    return decode
data = str(input('Введите строку: '))
encode_value = RLE_Encode(data)
print(f'encoded: {encode_value}')
decode_res = RLE_Decode(encode_value)
print(f'decoded: {decode_res}')