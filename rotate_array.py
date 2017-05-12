# Given an array and an integer k, rotate the array k times.
# Example:
# rotate_array([1,2,3,4,5], 2) #=> [3,4,5,1,2]
# rotate_array([1,2,3,4,5], 4) #=> [5,1,2,3,4]
# rotate_array([1,2,3,4,5], 5) #=> [1,2,3,4,5]


def rotate_array(array, n):
    return array[n:] + array[:n]

print rotate_array([1,2,3,4,5], 2)