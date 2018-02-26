'''
题目: 输入一个链表，从尾到头打印链表每个节点的值
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def printList(self, listNode):
        if not listNode:
            return []

        res = []
        node = listNode
        while node:
            res.append(node.val)
            node = node.next
        return res[::-1]
