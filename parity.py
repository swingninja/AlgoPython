def parity(dec):
    if dec == 0:
        return 0

    if dec == 1:
        return 1

    return bin(dec).count("1")

print parity(2)

