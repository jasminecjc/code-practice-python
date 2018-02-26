'''
题目: 编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。
给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，为0代表pop操
作，保证操作序列合法且一定含pop操作，请返回pop的结果序列。
'''

# -*- coding:utf-8 -*-


class TwoStack:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def twoStack(self, ope, n):
        res = []
        if n == 0:
            print 'empty queue'
            return
        for i in ope:
            if i > 0:
                self.stackPush.append(i)
            elif self.stackPop == []:
                while len(self.stackPush):
                    self.stackPop.append(self.stackPush.pop())
                res.append(self.stackPop.pop())
            else:
                res.append(self.stackPop.pop())
