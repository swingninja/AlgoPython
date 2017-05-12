# Given an array, find a pair in the array that would add up to the given sum.
# Example:
# find_pair(array = [1,2,3,4,5], sum = 5) => Pair: 1 and 4


def find_pair(array, sum):

    for i in range(len(array)):
        for j in range (i+1, len(array)):
            if array[i] + array[j] == sum:
                return [array[i], array[j]]


print find_pair([3, 1, 2, 3, 4 ,5], 5)
