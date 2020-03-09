def solve(s):

    #variables
    val = 0
    
    #converts all vowels to periods
    s = s.replace('a', '.')
    s = s.replace('e', '.')
    s = s.replace('i', '.')
    s = s.replace('o', '.')
    s = s.replace('u', '.')
    
    #splits the string on the periods and adds it to ret
    ret = s.split('.')
    
    #loop through all word in ret
    for x in ret:
        w_sum = 0
        #loop through letters in ret and get there values
        for i in x:
            w_sum += ord(i) - 96
        #finds the largest value and sets it to val
        if w_sum > val:
            val = w_sum
    
    #returns the largest value
    return val
