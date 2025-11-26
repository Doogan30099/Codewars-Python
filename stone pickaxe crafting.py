def stone_pick(arr):
    sticks = 0 
    cobbles = 0
    
    for r in arr:
        if r == 'Sticks':
            sticks += 1
        if r == 'Cobblestone':
            cobbles += 1
        if r == 'Wood':
            sticks += 4
    return min(sticks // 2, cobbles // 3)