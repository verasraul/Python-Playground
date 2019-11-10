__author__ = 'verasraul'


errormessage = "Cannnot divide"

try:
    3/0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is the Final \"Print Statement\"")