#Simple function takes two integers as arguments and divides the first int by the second int.
#Result will include remainders if any.


def divider (number1, number2):
    division = number1 // number2
    print (division)
    '''remainder = number1 % number2
    result = division, remainder
    if remainder is 0:
        print(division)
    else:
        print(result)'''


divider(3, 1)
