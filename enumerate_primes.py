# Given an integer n, enumerate all primes up to n.
#
# Example:
# n = 10
# primes = [2,3,5,7]


def enumerate_primes(max):
    primes = []

    if max < 2:
        return primes

    if max == 2:
        primes.append(max)
        return max

    primes.append(2)
    m = 3

    while m < max:
        counter = 1
        for n in primes:
            if m % n == 0:
                break

            if len(primes) == counter:
                primes.append(m)

            counter += 1

        m += 1

    return primes

print enumerate_primes(30)