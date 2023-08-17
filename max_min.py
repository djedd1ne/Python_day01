#!/usr/bin/python3

print("Enter list of numbers separated by spaces")
numbers = [int(x) for x in input().split()]
print("Max =", max(numbers))
print("Min =", min(numbers))