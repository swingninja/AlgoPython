# Given an integer whose digits are represented as an array, increment it and return the result.
#
# Example:
# increment_array([1,2,3]) #=> [1,2,4]
# increment_array([9,9,9]) #=> [1,0,0,0]


def increment_array(array):
    num = 0
    power = len(array) - 1
    array2 = []

    for i in range(len(array)):
        num = num + array[i] * pow(10, power)
        power -= 1

    num = num + 1

    while num is not 0:
        remainder = num % 10
        array2.append(remainder)
        num = num / 10

    return list(reversed(array2))

print increment_array([1,2,3])