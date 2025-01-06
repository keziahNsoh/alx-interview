#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys
import re


def is_valid_line(line):
    """Check if line matches required format"""
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'
    return re.match(pattern, line) is not None


def print_stats(total_size, status_codes):
    """Print statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function"""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1

            if not is_valid_line(line):
                continue

            try:
                parts = line.split()
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
