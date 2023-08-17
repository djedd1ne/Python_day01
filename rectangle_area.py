#!/usr/bin/python3

def rect_area(x, y):
    return x * y

print ("Enter Length and Breadth of Rectangle: ")
l = float(input("Length = "))
b = float(input("Breadth = "))
a = rect_area(l, b)
print ("Area =  ", a)