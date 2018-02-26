'''
题目: 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.stack = []
        self.cmp = []

    def push(self, node):
        self.stack.append(node)
        if not self.cmp:
            self.cmp.append(node)
        elif self.cmp[-1] < node:
            self.cmp.append(self.cmp[-1])
        else:
            self.cmp.append(node)

    def pop(self):
        self.stack.pop()
        self.cmp.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.cmp[-1]
