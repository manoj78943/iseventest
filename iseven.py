def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input always be an integer")
    return n % 2 == 0
