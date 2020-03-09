def no_odds(values):

    #variables
    ret = [] 
    
    #loop to check for even values and add it to the list
    for x in values:
        if x % 2 == 0:
            ret.append(x)
            
    # Return list of only even values
    return ret
