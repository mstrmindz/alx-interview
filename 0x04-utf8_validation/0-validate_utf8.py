#!/usr/bin/python3
""" contains the validUTF8 function"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    :param data:
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    labels = [False for n in data]

    n = 0
    while n < len(data):
        if data[n] < 128:
            labels[n] = True
            n += 1

        elif data[n] & 248 == 240:
            if n + 3 <= len(data) - 1:
                labels[n] = True
                n += 1
                for i in range(3):
                    if data[n + i] & 192 == 128:
                        labels[n + i] = True
                    else:
                        break
                n += 3
            else:
                break

        elif data[n] & 240 == 224:
            if n + 2 <= len(data) - 1:
                labels[n] = True
                n += 1
                for i in range(2):
                    if data[n + i] & 192 == 128:
                        labels[n + i] = True
                    else:
                        break
                n += 2
            else:
                break

        elif data[n] & 224 == 192:
            if n+1 <= len(data)-1:
                labels[n] = True
                n += 1
                if data[n] & 192 == 128:
                    labels[n] = True
                n += 1
            else:
                break
        else:
            break

    return all(labels)
