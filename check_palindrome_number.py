def check_palindrome(num):
    if num is None:
        return False

    # Single digit is a palindrome
    if num/10 == 0:
        return True

    # Extract digits and push onto stack
    stack = []
    num_copy = num

    while num_copy != 0:
        stack.append(num_copy % 10)
        num_copy = num_copy / 10

    # while stack is not empty
    while stack:
        if stack.pop() == num % 10:
            num = num / 10
        else:
            return False

    return True


print check_palindrome(123)
print check_palindrome(121)