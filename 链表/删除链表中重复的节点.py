'''
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重
复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处
理后为 1->2->5。
'''

# -*- coding:utf-8 -*-


class ListNode:
    def __init(self, x):
        self.val = x
        self.next = None


class Solution:
    def uniqueList(self, head):
        cur = head.next
        while cur:
            if cur.val == cur.next.val
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
