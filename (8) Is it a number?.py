def isDigit(string):
    #Check to see if string is an integer
    try:
        int(string)
        return True
    #String was no an integer
    except:
        #Check to see if string is a float
        try:
            float(string)
            return True
        #String is no a valid integer or float
        except:
            return False
