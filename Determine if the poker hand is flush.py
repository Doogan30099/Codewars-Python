def is_flush(cards):
    suit_set = set()
    for card in cards:
        suit = card[-1]
        suit_set.add(suit)
        print(suit_set)
    return len(suit_set) == 1