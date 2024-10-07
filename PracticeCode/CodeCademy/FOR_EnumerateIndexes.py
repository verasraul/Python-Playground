#Using the enumerate function

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')

#Enumerate works by supplying a corresponding index to each element in the list that you pass.
#Each time you go through the loop, index will be one greater, and item will be the next item in the sequence.
for index, item in enumerate(choices):
    print (index+1, item)