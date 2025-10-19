def insert_at_indexes(phrase, word, indexes): 
    for i in reversed(indexes): 
        phrase = phrase[:i] + word + phrase[i:]
    return phrase