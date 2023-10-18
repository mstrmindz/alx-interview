#!/usr/bin/python3

import sys
import re
import signal

# Define status codes to track
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables
line_count = 0
total_file_size = 0
status_code_counts = {code: 0 for code in status_codes}
current_line = ""

def print_statistics():
    global line_count, total_file_size, status_code_counts
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        current_line = line.strip()
        # Extract the file size and status code using regex
        match = re.search(r'\s(\d+)\s(\d+)$', current_line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            if status_code in status_codes:
                total_file_size += file_size
                status_code_counts[status_code] += 1
            line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C) by printing the statistics
    print_statistics()
