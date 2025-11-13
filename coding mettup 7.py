def find_senior(lst):
    senior_devs = []
    max_age = max(i['age'] for i in lst)
    for i in lst:
        if i['age'] == max_age:
            senior_devs.append(i)
    return senior_devs