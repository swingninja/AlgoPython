# For example: AA = 27, Z = 26


def spreadsheet_decoding(str):
    if str is None:
        return

    value = 0

    for c in str:
        value = (value * 26) + (ord(c.lower()) - 96)

    return value


print spreadsheet_decoding("ba")
