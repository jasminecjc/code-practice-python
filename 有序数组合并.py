'''
题目: 有两个从小到大排序以后的数组A和B，其中A的末端有足够的缓冲空容纳B。
请编写一个方法，将B合并入A并排序。
给定两个有序int数组A和B，A中的缓冲空用0填充，同时给定A和B的真实大小int n
和int m，请返回合并后的数组。
'''

# -*- coding:utf-8 -*-


class Merge:
    def mergeAB(self, A, B, n, m):
        index = n + m - 1
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[index] = B[j]
                j -= 1
            else:
                A[index] = A[i]
                i -= 1
            index -= 1
        if j >= 0:
            A[:j + 1] = B[:j + 1]
        return A
