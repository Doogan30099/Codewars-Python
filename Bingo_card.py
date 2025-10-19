import random 

def get_bingo_card():
    
    card = {
        "B": random.sample(range(1, 16), 5),
        "I": random.sample(range(16, 31), 5),
        "N": random.sample(range(31, 46), 4),
        "G": random.sample(range(46, 61), 5),
        "O": random.sample(range(61, 76), 5)
    }


    bingo_card = []
    for letter in "BINGO":
        for number in card[letter]:
            bingo_card.append(f"{letter}{number}")  
    return bingo_card
