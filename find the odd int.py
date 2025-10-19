def find_it(seq):
    count = 0 
    for x in seq:
        count = seq.count(x)
        if count % 2 != 0:
            return x
