#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n):
    if n <= 0:
        return 0

    # Edge case: If n is a power of 2, we can achieve it with only 2 operations
    if (n & (n - 1)) == 0:
        return 2

    # Initialize the number of operations to 0
    operations = 0

    # Keep dividing n by 2 until it becomes 1
    while n > 1:
        # If n is odd, we need an extra paste operation
        if n % 2 != 0:
            operations += 1
            n -= 1
        # Divide n by 2
        n //= 2
        # Increment the number of operations
        operations += 1

    # We need one more paste operation to get the final result
    operations += 1

    return operations
