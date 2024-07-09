#!/usr/bin/env python3
# Author ID: kcpatel15

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, OSError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # this works
    print(add('10', 5))                      # this works
    print(add('abc', 5))                     # this is exception
    print(read_file('seneca2.txt'))          # this works
    print(read_file('file10000.txt'))        # this is exception
