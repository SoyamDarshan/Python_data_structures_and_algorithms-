# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:42:08 2018

@author: ThinkPad


How do you find the missing number in a given integer array of 1 to 100?
"""


a = [x for x in range(1, 11)]
asum = sum(a)
a1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
a1sum = sum(a1)

missingnumber = asum - a1sum
print(missingnumber)
