def hero(bullets, dragons):
    #variables
    b = bullets
    d = dragons
    bn = d * 2
    
    #statements to check to see if hero will survive
    if b >= bn:
        return True
    else:
        return False
