#given function
def rgb(r, g, b):
    #fuunction to convert decimal to hex
    def decToHex(c):
        #checks the input and return a hex value
        if (c > 255):
            return "FF"
        #checks the conditions and returns a hex value
        if (c < 0):
            return "00"
        #catch condition to return a hex value
        else:
            return hex(c)[2:].zfill(2).upper()

    #calls the decimal to hex function to convert rgb values to hex
    return decToHex(r) + decToHex(g) + decToHex(b)
