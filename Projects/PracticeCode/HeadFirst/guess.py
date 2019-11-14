from random import randint

print('WELCOME!')
guess = 0
secret = randint (1,20)

while guess != secret:
    g = input('Guess the number: ')
    guess = int(g)
    if guess == secret:
        print('You Win!')
    else:
        if guess < secret:
            print('Too Low!')
        if guess > secret:
            print('Too High!')
            
print('Game Over!')


