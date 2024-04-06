def unique_list(l):
    x =  []
    
    for e in l:
        
        if e not in x:
            x.append(e)
        
    return x

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))        