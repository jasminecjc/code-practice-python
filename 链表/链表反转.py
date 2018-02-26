#  -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reserverList1(self, head):
        # 非递归
        if not head or not head.next:
            return []
        else:
            prev = head
            cur = head.next

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            head.next = None
            return prev

    def reserverList2(self, head):
        # 递归
        if not head or not head.next:
            return head
        else:
            newHead = self.reserverList2(head.next)
            head.next.next = head
            head.next = None
            return newHead
