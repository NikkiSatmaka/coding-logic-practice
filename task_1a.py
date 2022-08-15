#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) < 1:
        exit  # list has to contain at least 1 element

    # prepare a list to store the correct sequence
    # since it's binary, there are two possible correct sequence
    X1 = []
    X2 = []
    for index in range(len(A)):
        if index % 2 == 0:
            X1.append(0)
            X2.append(1)
        else:
            X1.append(1)
            X2.append(0)

    # # debug print out the lists
    # print(A)
    # print(X1)
    # print(X2)

    # find the absolute difference between the proper sequence and the original sequence
    X1diff = np.abs(np.array(A) - np.array(X1))
    X2diff = np.abs(np.array(A) - np.array(X2))

    # # debug print out the difference and the count of it
    # print('-' * 80)
    # print(X1diff, np.count_nonzero(X1diff))
    # print(X2diff, np.count_nonzero(X2diff))

    # return the one which has the lowest number of differences
    return min(np.count_nonzero(X1diff), np.count_nonzero(X2diff))


A = [1, 0, 1, 0, 1, 1]
# A = [1, 1, 0, 1, 1]
# A = [0, 1, 0]
# A = [0, 1, 1, 0]

print(solution(A))
