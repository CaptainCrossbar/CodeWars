def pig_it(text):
    #creates a case for possible english characters and numbers
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    
    #splits text into words
    text = text.split(" ")
    
    #creates an empty list
    new = []
    
    #loop to go through words to re-order them
    for i in range(len(text)):
        
        #checks to see if in case and is only 1 character long, adds ay
        if text[i] in alpha and len(text[i]) == 1:
            text[i] = text[i]+ "ay"
        
        #checks to see if word is greater than 2 characters, moves first letter to the back of word and adds ay
        elif len(text[i]) >= 2:
            text[i] = text[i][1: -1]+ text[i][-1]+  text[i][0]+ "ay"
        
        #condition if other two arernt meet
        else: 
            text[i] = text[i]
        
        #adds the change to the list new
        new.append(text[i])
    
    #joins the words in list new and returns it
    return " ".join(new)
