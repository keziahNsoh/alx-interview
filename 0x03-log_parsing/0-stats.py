#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_read = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up signal handling for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            lines_read += 1
            total_file_size += int(match.group(4))  # File size is the fourth group
            status_code = int(match.group(3))  # Status code is the third group
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Print statistics every 10 lines
            if lines_read % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
