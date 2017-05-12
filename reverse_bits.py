def reverse_bits(dec):
    if dec == 0:
        return 0

    if dec == 1:
        return 1

    result = 0

    while dec > 0:
        value = dec & 1

        result << 1

        if value == 1:
            result = result ^ 1     # Injects 1 at the LSB

        dec = dec >> 1

    return result


print reverse_bits(4)  # answer should be 1 (4 is 100, become 001)
