#!/usr/bin/python3
def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0
    
    for byte in data:
        # Get the last 8 bits of the byte
        byte &= 0xFF
        
        # Check the number of bytes in the UTF-8 character
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue  # 1-byte character (ASCII)
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 byte
        
        else:
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    return num_bytes == 0  # All characters must be completed

