def which_appears_twice(array, n):
    expected_sum = (n * (n+1))/2
    real_sum = 0

    for e in array:
        real_sum += e

    print real_sum, expected_sum

    return real_sum - expected_sum

print which_appears_twice([1, 2, 2, 3], 3)