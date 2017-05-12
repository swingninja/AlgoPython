# Given a number encode it into a spreadsheet column title.
# For example: 27 = AA, 1 = A


def spreadsheet_encoding(num):
    if num == 0:
        return ''

    chars = ''

    while num > 0:
        chars = chars + chr(num % 26 + 96)
        num = num / 26

    return chars

print spreadsheet_encoding(1)
print spreadsheet_encoding(27)



