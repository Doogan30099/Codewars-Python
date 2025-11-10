def high_and_low(numbers):
    x = max(map(int, numbers.split()))
    y = min(map(int, numbers.split()))
    return f"{x} {y}"