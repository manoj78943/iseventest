def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0
