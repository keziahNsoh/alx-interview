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
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \["
    r'(.*?)\] "GET /projects/260 HTTP/1\.1" '
    r"(\d{3}) (\d+)"
)


def print_stats():
    """Print the collected statistics."""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line
try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            file_size = int(file_size)
            status_code = int(status_code)

            # Update metrics
            total_file_size += file_size
            status_codes[status_code] += 1
            lines_read += 1

            # Print stats every 10 lines
            if lines_read % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
except Exception:  # Catch all other exceptions
    pass  # Handle exceptions if necessary
