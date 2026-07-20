def fibonacci(n):
    """
    Return the nth Fibonacci number.

    Time Complexity: O(n)
    Space Complexity: O(1)
    Optimal Time Complexity: O(n)
    """

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current