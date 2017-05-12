def swap_bits(dec, n1, n2):
    # find the 1st bit by shifting dec n1 steps to the rightmost side
    bit1 = (dec >> n1) & 1

    # find the 2nd bit by shifting dec n2 steps to the rightmost side
    bit2 = (dec >> n2) & 1

    # XOR bit1 and bit2
    x = bit1 ^ bit2

    # Put the xor bit back to their original positions
    x = (x << n1) | (x << n2)

    # XOR x with the original number to swap the bits
    return dec ^ x


print swap_bits(28, 0 , 3) # output is 21