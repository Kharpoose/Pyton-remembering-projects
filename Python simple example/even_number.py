def even_number(l):
    x = []
    
    for e in l:
        
        if e % 2 == 0:
            x.append(e)
            
    return x


print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]))            