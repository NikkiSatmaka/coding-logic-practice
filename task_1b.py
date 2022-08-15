#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) < 1:
        exit  # list has to contain at least 1 element

    # prepare a list storing the correct sequence
    # since it's binary, there are two possible correct sequence
    # [0, 1] and [1, 0] are both correct for two-coin toss sequence
    X1 = [0 if index % 2 == 0 else 1 for index, element in enumerate(A)]
    X2 = [1 if index % 2 == 0 else 0 for index, element in enumerate(A)]
    count1 = 0
    count2 = 0

    # # debug print out the lists
    # print(A)
    # print(X1)
    # print(X2)

    # count the number of differences for each index
    for index in range(len(A)):
        if A[index] != X1[index]:
            count1 += 1
        if A[index] != X2[index]:
            count2 += 1

    # # debug print out the number of differences
    # print('-' * 80)
    # print(count1)
    # print(count2)

    # return the one which has the lowest number of differences
    return min(count1, count2)


A = [1, 0, 1, 0, 1, 1]
# A = [1, 1, 0, 1, 1]
# A = [0, 1, 0]
# A = [0, 1, 1, 0]

print(solution(A))
