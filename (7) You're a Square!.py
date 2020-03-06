#allows the square root operation
import math

def is_square(n):
    #checks to see if the number is positive
    if n >= 0:
        #checks to see if the number is a square
        if math.sqrt(n) % 1 == 0:
            return True
        #if number has a remainder, then it is not a square
        else:
            return False
    #if number was not positive, then it was a negative number
    else:
        return False
