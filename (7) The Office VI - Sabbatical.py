def sabb(s, value, happiness):

    #defines varibles that will be used
    str = s
    val = value
    happ = happiness
    sat = 0
    
    #goes through and checks the string for the characters that are weighted
    for index in range ( len ( str ) ):
        if str[index] == 's'or str[index] == 'a'or str[index] == 'b'or str[index] == 'b'or str[index] == 'a'or str[index] == 't'or str[index] == 'i'or str[index] == 'c'or str[index] == 'a'or str[index] == 'l' or str[index] == 'I': 
            sat += 1
        #print ( str[index] )
        
    #if statement to check point values, if meets criteria, get to go; else back to desk 
    if val + happ + sat > 22:
        return 'Sabbatical! Boom!'
    else:  
        return 'Back to your desk, boy.'
