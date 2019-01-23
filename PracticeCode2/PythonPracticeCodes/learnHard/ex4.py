# place all information into varibles
# amount of cars
cars = 100
# amount of space in car
space_in_a_car = 4.0
# 4.0 means 4 car seats/persons

# how many drivers?
drivers = 30

# amount of passengers
passengers = 90

# cars left to without drivers
cars_not_driven = cars - drivers

# cars being driven
cars_driven = drivers

# Amount of people transported 
carpool_capacity = cars_driven * space_in_a_car

# Average amount of passengers per car
avg_passengers_per_car = passengers / cars_driven

print "There are %s cars available." % cars
print "There are only %s drivers available." % drivers
print "There will be %s empty cars today." % cars_not_driven
print "We can transport %s people today." % carpool_capacity
print "We have %s to carpool today." % passengers
print "We need to put about %s in each car." % avg_passengers_per_car