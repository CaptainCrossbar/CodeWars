def capitalize(s):
    
    #variables
    result = []
    result2 = []
    
    #loop to go through string
    for i,x in enumerate(s):
      
        #statements to convert upper to lower or lower to upper. Allows for alternating cases
        if  i % 2 == 0:
            result.append(x.upper())
            result2.append(x.lower())
        else:
            result.append(x.lower())
            result2.append(x.upper())
  
    #combines the results into a list to be returned 
    ret = []
    ret.append(''.join(result))
    ret.append(''.join(result2))

    return ret
