# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:41:38 2018

@author: ThinkPad
"""


def insertion_sort(A):

    for k in range(len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1

        A[j] = cur
        print(A)
    return A    


print(insertion_sort([5, 6, 7, 3, 22, 3, 3, 6, 7, 8, 3, 2, 1]))
