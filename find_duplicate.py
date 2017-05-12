# Given an array that has elements in the range 1..n. There is 1 duplicate element in it.
# Find the duplicate element using only O(1) space.
#
# Example:
# i/p: 2,4,6,4,5,1,3
# o/p: 4 => duplicate element

def find_duplicate(array):
    for item in set(array):
        if array.count(item) > 1:
            return item

print find_duplicate([2,4,6,4,5,1,3])