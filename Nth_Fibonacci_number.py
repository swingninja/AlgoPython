def nth_fibonacci_number(n):
    if n == 0 or n == 1:
        return n

    i = 2
    current = 1
    prev = 0

    while i <= n:
        fib = current + prev
        prev = current
        current = fib
        i += 1

    return fib

print nth_fibonacci_number(2)
