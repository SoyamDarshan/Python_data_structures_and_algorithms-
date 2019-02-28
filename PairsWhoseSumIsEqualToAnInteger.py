# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:16:24 2018

@author: ThinkPad

How do you find all pairs of an integer array whose sum is
equal to a given number?

"""

a = [2, 321, 43, 14, 12, 32, 13, 21, 12, 13, 13]
givensum = 26

i = 0
j = len(a) - 1

a.sort()

while i < j:
    if a[i] + a[j] == givensum:
        print('{0} {1}'.format(a[i], a[j]))
        i += 1
        j -= 1
    elif a[i] + a[j] < givensum:
        i += 1
    elif a[i] + a[j] > givensum:
        j -= 1
