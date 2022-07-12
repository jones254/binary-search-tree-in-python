def game( hc, hb, ac, ab):
    
    home = hc + hb
    
    away = ac + ab
    
    dif = abs(home - away)  
    return home, dif, away,      

    

score = game(67, 60, 47, 73)  
print(score) 