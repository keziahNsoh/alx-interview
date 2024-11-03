#!/usr/bin/python3


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    expected_bytes = 0

    for num in data:
        byte = num & 0xFF

        if expected_bytes == 0:
            if (byte >> 7) == 0b0:  # 1-byte character
                expected_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                expected_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                expected_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                expected_bytes = 3
            else:
                return False  # Invalid start byte
        else:
            if (byte >> 6) != 0b10:  # Continuation byte check
                return False

        expected_bytes -= 1

    return expected_bytes == 0
