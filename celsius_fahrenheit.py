#!/usr/bin/python3

def celsius_fahrenheit(celsius):
    return celsius * 1.8 + 32

celsius = float(input ("Enter a celsius temperature: "))
print ("Fehrenheit temperature = ", celsius_fahrenheit(celsius))