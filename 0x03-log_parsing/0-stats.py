#!/usr/bin/python3
"""Module for parsing logs from stdin and computing metrics"""
import sys


def print_stats(total_size, status_codes):
    """Print statistics about log data"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Process log input and compute metrics"""
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
            try:
                parts = line.split()
                # Check log format
                if (
                    len(parts) != 9
                    or parts[5] != '"GET'
                    or parts[6] != "/projects/260"
                    or parts[7] != 'HTTP/1.1"'
                ):
                    continue
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
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
