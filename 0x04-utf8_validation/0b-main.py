#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-decode_utf8').validUTF8


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))


data = [229, 173, 151]
print(validUTF8(data))

data = [207, 191]
print(validUTF8(data))

data = [229, 174, 152, 65]
print(validUTF8(data))


data = [226, 130, 172]
print(validUTF8(data))

data = [229, 173, 151, 32, 80, 121, 116, 104,
        111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))


data = [240, 159, 164, 159]
print(validUTF8(data))

data = [244, 191, 191, 191]
print(validUTF8(data))
