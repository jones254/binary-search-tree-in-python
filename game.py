def game(hs, hc, asc, ac):
    h = hs + (100 - asc)
    hh = hc + (100 - ac)
    a = asc + (100 - hs)
    aa = ac + (100 - hc)

    if hh > aa and h > a and h > asc*2:
        return f' home {hh}, {h}'
    elif aa > hh and a > h and a > hs*2:
        return f' away {aa}, {a}'  
    else :
        return False
score = game(13, 25, 75, 50) 
print(score)       