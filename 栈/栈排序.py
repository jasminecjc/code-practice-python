'''
题目: 请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多
只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。给定
一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请
返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。
注: python模拟栈操作很慢，直接用sort
'''


# -*- coding:utf-8 -*-
class TwoStacks:
    def __init__(self):
        self.cmpStack = []

    def twoStacksSort(self, numbers):
        while len(numbers):
            cur = numbers[0]
            numbers.pop(0)
            if self.cmpStack == [] or cur <= self.cmpStack[-1]:
                self.cmpStack.append(cur)
            else:
                while len(self.cmpStack):
                    numbers.append(self.cmpStack[-1])
                    self.cmpStack.pop()
                self.cmpStack.append(cur)
        return self.cmpStack
