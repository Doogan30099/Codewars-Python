def all_continents(lst): 
    continents = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}
    devloc = {i['continent'] for i in lst}
    if continents == devloc: 
        return True 
    return False
    
    