# Given a key, delete all occurrences of it from the array
#
# Example:
# delete_key([5,1,6,3,4,5,8,3,5], 5) #=> [1,6,3,4,8,3]
# delete_key([5], 5) #=> []


def delete_key(array, key):
    array2 = []

    for i in array:
        if i is not key:
            array2.append(i)

    return array2


print delete_key([5,1,6,3,4,5,8,3,5], 5)