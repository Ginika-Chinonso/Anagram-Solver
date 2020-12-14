#!/bin/python3

from itertools import permutations
pwd = input('Enter password: ')
print('Password combination: ')
permlist = list(permutations(pwd))
# print(permlist)
for p in permlist:
    wrdlst = list(p)
    wrd = ''.join(wrdlst)
    print(wrd)