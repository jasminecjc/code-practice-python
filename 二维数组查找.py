'''
题目: 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从
上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数 
思路: 从右上角开始，比当前数大往下移，比当前数小往左移
'''

# -*- coding:utf-8 -*-


class Solution:
    def func(self, arr, target):
        row, col = len(arr), len(arr[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if arr[i][j] > target:
                j -= 1
            else if arr[i][j] < target:
                i += 1
            else:
                return True
        return False
