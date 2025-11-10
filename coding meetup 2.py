def greet_developers(lst): 
    for i in lst:
        name = i['firstName']
        language = i['language']
        greeting = f'Hi {name}, what do you like the most about {language}?'
        i["greeting"] = greeting
    return lst