def solution(number):
    multiples = []
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
    for i in multiples:
        sum += i
    return sum