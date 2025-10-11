def find_average(numbers):
    sum = 0
    average = 0
    for number in numbers:
        sum += number
        average = sum / len(numbers)
    return average