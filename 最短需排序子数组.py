'''
题目: 对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。
给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。
(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。
'''
# -*- coding:utf-8 -*-


class Subsequence:
    def shortestSubsequence(self, A, n):
        min, max = A[n - 1], A[0]
        start = end = 0
        for i in range(1, n):
            if max <= A[i]:
                max = A[i]
            else:
                end = i
        for j in range(n - 2, -1, -1):
            if min >= A[j]:
                min = A[j]
            else:
                start = j
        if start == 0 and end == 0:
            return 0
        else:
            return end - start + 1
