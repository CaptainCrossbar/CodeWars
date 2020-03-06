def basic_op(operator, value1, value2):
    #Checks to see if the operation is addition
    if operator == '+':
        #returns the value of value1 plus value2
        return value1 + value2
    #Checks to see if the operation is subtraction
    elif operator == '-':
        #returns the value of value1 minus value2
        return value1 - value2
    #Checks to see if the operation is multiplication
    elif operator == '*':
        #returns the value of value1 times value2
        return value1 * value2
    #Operation will be division if all other statements were not true
    else:
        #returns the value of value1 divided value2
        return value1 / value2
  
