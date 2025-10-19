import random 

def get_bingo_card():
    
    columns = {
        "B": random.sample(range(1, 15), 5),
        "I": random.sample(range(16, 30), 5),
        "N": random.sample(range(31, 45), 4),
        "G": random.sample(range(46, 60), 5),
        "O": random.sample(range(61, 75), 5)
    }


    bingo_card = []

    for i in range(5):
        row = []
        for col in ["B", "I", "N", "G", "O"]:
            if col == "N" and i == 2:
                row.append("FREE")
            else:
                row.append(columns[col][i if col != "N" or i < 2 else i - 1])
        bingo_card.append(row)
    return bingo_card


