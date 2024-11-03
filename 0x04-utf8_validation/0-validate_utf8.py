#!/usr/bin/python3

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if the data is valid UTF-8 encoding, otherwise False.
    """
    expected_bytes = 0

    for num in data:
        byte = num & 0xFF  # Mask to get the last 8 bits

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
            if (byte >> 6) != 0b10:  # Check if it's a continuation byte
                return False

        expected_bytes -= 1  # Decrement the expected bytes count

    return expected_bytes == 0  # Return True if all expected bytes are accounted for

