def get_first_python(users):
    for u in users:
        name = u['first_name']
        country = u['country']
        if u['language'] == 'Python':
            return f'{name}, {country}'
    return 'There will be no Python developers'
        