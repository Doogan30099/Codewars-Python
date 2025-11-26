def is_age_diverse(lst):
    age_groups = {
        "teens": range(10, 20),
        "twenties": range(20, 30),
        "thirties": range(30, 40),
        "forties": range(40, 50),
        "fifties": range(50, 60),
        "sixties": range(60, 70),
        "seventies": range(70, 80),
        "eighties": range(80, 90),
        "nineties": range(90, 100),
        "centenarian": range(100, 200)
    }

    found = set()

    for person in lst:
        age = person['age']
        for group, rng in age_groups.items():
            if age in rng:    
                found.add(group)

    return len(found) == len(age_groups)
