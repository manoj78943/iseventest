def is_even(n):
    if isinstance(n, bool):
        raise ValueError("Input cannot be a boolean")
    if not isinstance(n, int):
        raise ValueError("Input always be an integer")
    return n % 2 == 0


# test cases added
