def to_alternating_case(string):
    
    #variables
    result = []
    
    #loop to go through string
    for x in string:
        
        #checks to see if x is lowercase or uppercase and changes it to the opposite
        if x.islower():
            result.append(x.upper())
        else:
            result.append(x.lower())

    #puts the string back together after the changes happened
    return ''.join(result)
