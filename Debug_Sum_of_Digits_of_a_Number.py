def get_sum_of_digits(num):
    sum = 0
    digits = str((num))
    for d in digits:
        sum += int(d)
    return sum