#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

total_size = 0
counter = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 2:
            code = line_list[-2]
            size = line_list[-1]
            if code in codes:
                codes[code] += 1
            total_size += int(size)
            counter += 1

        if counter == 10:
            print("File size: {:d}".format(total_size))
            for k, v in sorted(codes.items()):
                if v != 0:
                    print("{}: {:d}".format(k, v))
            counter = 0

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))
