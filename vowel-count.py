def get_count(sentence):
    vowels = ['a','e','i','o','u']
    count = 0
    for x in sentence:
        if(x in vowels):
            count = count + 1
            
    return count 