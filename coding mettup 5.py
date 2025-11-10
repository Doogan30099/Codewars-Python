def count_languages(lst):
    languages = {}
    for i in lst:
        lang = i['language']
        languages[lang] = languages.get(lang, 0) + 1
    return languages