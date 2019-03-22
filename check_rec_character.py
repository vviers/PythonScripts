# A Very Basic Coding Interview Question

import sys
def checker(string):
    '''Return the first reccuring character in a given string.'''
    if type(string) != str:
        raise TypeError("Please provide a string")
    tracker = {}
    for s in string:
        if s in tracker:
            print("{} is the first recurring character.".format(s))
            return s
        else:
            tracker[s] = 1
    print("None found.")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\n\tpython check_rec_character.py mystringiwhishtotest")
        exit()
    usr_string = sys.argv[1]
    checker(usr_string)

