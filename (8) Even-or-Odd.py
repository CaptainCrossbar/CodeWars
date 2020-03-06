def even_or_odd(number):
    #checks to see if the number is even by doing modulus 2. if reminder is 0, it is even.
    if number % 2 == 0:
        return 'Even'
    #if mod 2 had a remainder, the number is odd
    else:
        return 'Odd'
