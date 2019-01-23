__author__ = 'verasraul'

# Everything Lists


# What they are?"
'''list is a mutable sequence type'''

# empty list:
empty_list = []

# non-empty list:
non_empty = [1, 2, 3, 4]

# How to add:
# adds to end of list
non_empty.append(5)
if 5 in non_empty:
    print("5 is in non_empty")
else:
    print("5 is not in non_empty")

# adds in front of specified position
# first argument given is the index
non_empty.insert(0, -1)
if non_empty.index(-1) == 0 and non_empty[0] == -1:
    print()
else:
    print()

# concatenate lists:

# first method
list_one = [1,2,3]
list_two = [4,5,6]
list_one.extend(list_two)
print(list_one)

# second method
list_one + list_two
print(list_one)

# remove items
# raises error if item is not found in list.
non_empty.remove(4)
if non_empty.count(4) == 0:
    print("The number 4 is not in the list")
else:
    print("The number 4 is in position %s" % non_empty.index(4))

# removes and returns item in list.
# Raises KeyError if the set is empty.
non_empty.pop(2)
if non_empty[2] == 4:
    print ("The item #3 has been popped out of the list, %s." % non_empty)
else:
    print (non_empty)


# update items:
# updates item in given position on the list
# returns an error if index isn't in the list
non_empty[1] = 4
print non_empty

# adds in front of specified position
# first argument given is the index
non_empty.insert(0, -1)
if non_empty.index(-1) == 0 and non_empty[0] == -1:
    print()
else:
    print()


# replace items:
# returns an error if index isn't in the list
non_empty[1] = 4
print non_empty



# How to loop through them:
# loops through every item and does something per each loop.
for x in non_empty:
    print(x)


# will continue execution as long as the statement is true.
while 1 in non_empty is not 0:
    print 1


# How to search for things in them:
# Will return boolean true/false if it does/doesn't find item in list.
1 in non_empty

# Will check to see if item is in list then do something.
if 1 in non_empty:
    print("#1 is found at index %s in non_empty list" % non_empty.index(1))

# When to use each (performance gains, etc..)

