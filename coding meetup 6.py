def is_same_language(lst):
    return len({i['language'] for i in lst}) == 1