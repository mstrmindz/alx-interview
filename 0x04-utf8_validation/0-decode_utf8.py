#!/usr/bin/python3
""" contains the validUTF8 function"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    :param data:
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    a = 0
    if not isinstance(data, list):
        return False

    if len(data) < 1:
        return False

    labels = [False for n in range(len(data))]

    n = 0
    while n < len(data):

        if data[n] < 128:
            labels[n] = True
            print(chr(data[n]), end='')
            n += 1

        elif data[n] & 248 == 240:
            if n + 3 <= len(data) - 1:
                labels[n] = True
                a = (data[n] & 15) << 18
                n += 1

                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127) << 6
                    a += b
                    n += 1
                else:
                    break
                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127) << 6
                    a += b
                    n += 1
                else:
                    break
                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127) << 6
                    a += b
                    n += 1
                else:
                    break
                print(chr(a), end='')

            else:
                break

        elif data[n] & 240 == 224:
            if n + 2 <= len(data) - 1:
                labels[n] = True
                a = (data[n] & 31) << 12
                n += 1
                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127) << 6
                    a += b
                    n += 1
                else:
                    break
                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127)
                    a += b
                    n += 1
                else:
                    break

                print(chr(a), end='')

            else:
                break

        elif data[n] & 224 == 192:
            if n + 1 <= len(data) - 1:
                labels[n] = True
                a = (data[n] & 63) << 6
                n += 1
                if data[n] & 192 == 128:
                    labels[n] = True
                    b = (data[n] & 127)
                    a += b
                    print(chr(a), end='')
                    n += 1
                else:
                    break
        else:
            break

    print('')

    return all(labels)
