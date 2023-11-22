#!/usr/bin/python3


import string
def print_alphabet():
    for letter in range(97, 123):
        print(chr(letter), end='')
    print()

def print_alphabet1():
    # Printing the lowercase alphabet in reverse
    print(string.ascii_lowercase[::-1])


def create_alphabet():
    alphabet = ''
    for i in range(97, 123):
        alphabet += chr(i)
    return alphabet

alphabet = create_alphabet()

slice_alphabet = alphabet.slice(0, 26)
print(slice_alphabet)



