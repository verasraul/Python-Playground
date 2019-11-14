#Function to verify if number is prime

def is_prime(x):
    if x < 2:#Because numbers less than 2 are not prime.
        return False
    elif x == 2:#Because 2 is prime.
        return True
    else:
        for n in range(2, x):#All prime numb are divisible by 1 and itself. Do
            #not want to test for those 2 numbers. start with 2 until/not incl.
            #X and excluding 1(x-1).
            if x % n == 0:#If any numbers between 2 'til/not incl. X are evenly
                #divisible, numb cannot be prime, prime numb are only evenly
                #divisible by 1 and itself which are excluded from the function.
                return False
        else:
            return True
                
print(is_prime(0))
