def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    
    #variables
    bs = blue_start
    rs = red_start
    bp = blue_pulled
    rp = red_pulled
    
    #calculates blue and red left
    bl = bs - bp
    rl = rs - rp
    
    #calculate guess blue stat
    gb = bl / (bl + rl)
    
    return gb
