# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:14:36 2018

@author: ThinkPad

How do you find the largest and smallest number in an unsorted integer array?

"""


def maxi(num, max):
    if max < num:
        max = num
    return max


def mini(num, min):
    if min > num:
        min = num
    return min


a = [2, 321, 43, 14, 12, 32, 13, 21, 12]
max = a[0]
min = a[0]

for i in a:
    max = maxi(i, max)
    min = mini(i, min)

print(max)
print(min)
