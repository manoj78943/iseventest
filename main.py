from iseven import is_even

a = [4, -6, 0, 5, 3.5, "hello", True, None, False]

for num in a:
    try:
        result = is_even(num)
        print(f"{num} is even: {result}")
    except ValueError as e:
        print(f"Error for input - '{num}': {e}")
