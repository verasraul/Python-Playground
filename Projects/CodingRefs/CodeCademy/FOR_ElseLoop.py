fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
    break


#MODIFIED WITHOUT "BREAK"

'''fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    print 'A', f
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
else:
    print 'A fine selection of fruits!'
'''

#CREATED OWN
'''store = ['Nike', 'Adidas', 'Valentino', 'Puma']

brand = raw_input('What brand are you looking for? ')

for a in store:
    print 'We have ' + a
else:
    if brand != a:
        print 'Sorry, we don\'t have that in stock right now'
'''