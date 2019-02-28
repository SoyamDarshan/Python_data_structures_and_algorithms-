# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:43:27 2019

@author: ThinkPad

multiple duplicates in an array
"""


def print_repeating(arr, size):

    print("the repeating elements are: ")

    for i in range(0, size):
        print(i)
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
        print(arr)


arr = [2, 1, 3, 1, 3, 6, 6]
arr_size = len(arr)
print(arr)
print_repeating(arr, arr_size)
