# Create a program that takes some text and returns a list of all the characters in the text that aren't vowels,
# sorted in alphabetical order.
# 
# You can either enter the text from the keyboard or initialise a string variable with the string. 

strings  = set(input("Write a text "))
vowels = frozenset("aeiou")

for vowel in vowels:
    if vowel in strings:
        print(sorted(strings.difference(vowels)))
