# Given a sorted array with duplicate elements, eliminate the duplicate elements in place.
#
# Example:
# i/p: [1,1,1,2,3,4,4,4,5,6,7,7,7]
# o/p: [1,2,3,4,5,6,7]


def delete_duplicate(array):
    uniq = []

    for i in array:
        if i not in uniq:
            uniq.append(i)

    return uniq


print delete_duplicate([1,1,1,2,3,4,4,4,5,6,7,7,7])