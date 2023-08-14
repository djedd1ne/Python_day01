#!/usr/bin/python3

n = int(input ("Enter a whole number: "))
while (n < 0):
    n = int(input ("Enter a whole number: "))
total_sum = 0
for i in range(0, n+1):
    total_sum += i
print ("total sum = ", total_sum)