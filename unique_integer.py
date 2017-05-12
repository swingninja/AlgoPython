# Given the array of IDs, which contains many duplicate integers and one unique integer,
# find the unique integer. All integers have one duplicate except the unique integer.


def unique_integer(array):
    unique = []

    for i in array:
        if i not in unique:
            unique.append(i)
        else:
            unique.pop()

    return unique[0]


print unique_integer([1,1,2,2,5,3,3,3,4,4])