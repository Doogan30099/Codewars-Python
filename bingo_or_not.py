def bingo(array): 
    bingo_numbers = [2, 9, 14, 7, 15]
    if all(n in array for n in bingo_numbers):
        return "WIN"
    else:
        return "LOSE"