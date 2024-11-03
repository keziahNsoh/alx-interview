#!/usr/bin/python3


def validUTF8(data):
    # It shows if a given data set represents a valid UTF-8 encoding
    expected_bytes = 0

    for number in data:
        if expected_bytes != 0:
            # We are expecting continuation bytes
            if not (128 <= number < 192):  # 10xxxxxx
                return False
            expected_bytes -= 1
        else:
            if number < 128:  # 0xxxxxxx
                continue
            elif 192 <= number < 224:  # 110xxxxx
                expected_bytes = 1
            elif 224 <= number < 240:  # 1110xxxx
                expected_bytes = 2
            elif 240 <= number < 248:  # 11110xxx
                expected_bytes = 3
            else:
                return False  # Invalid starting byte
    return expected_bytes == 0
