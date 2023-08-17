#!/usr/bin/python3

def is_even(x):
    if (x % 2 == 0):
        return True
    else:
        return False

number = int(input("Enter a number: "))
if (is_even(number)):
    print (str(number), "is even")
else:
    print (str(number), "is odd")