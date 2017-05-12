# Write a function that flattens an Array of Array objects into a flat Array.
# Your function must only do one level of flattening.

def array_flatten(array):
    result = []

    for element in array:
        if isinstance(element, list):
            for in_element in element:
                result.append(in_element)
        else:
            result.append(element)

    return result

print array_flatten([[3,2],1])