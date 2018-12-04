# -*- coding:utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
class Solution:
  def add(self, l1, l2):
    if l1 == None or l2 == None:
      return l1 or l2
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while l1 and l2:
      val = carry + l1.val + l2.val
      if val >= 10:
        carry = 1
        val -= 10
      else:
        carry = 0
      cur.val = val
      l1 = l1.next
      l2 = l2.next
      cur = cur.next
    return dummy