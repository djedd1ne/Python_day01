#!/usr/bin/python3

def is_palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
        return True

ans = input("Enter a word to check Palindrome: ")
if (is_palindrome(ans)):
    print("Yes, the word", ans, "is a Palindrome")
else:
    print("No, the word", ans, "is not a Palindrome")