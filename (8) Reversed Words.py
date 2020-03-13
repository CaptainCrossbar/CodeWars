def reverseWords(str):

    #make arr variable and give it the split of the string
    arr = str.split()

    #takes arr and reverses it and places it in rev
    rev = arr[::-1]

    #joins rev together to make string and returns it
    return " ".join(rev)
