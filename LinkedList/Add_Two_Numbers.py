# -*- coding:utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
  def add(self, l1, l2):
    if l1 == None or l2 == None:
      return l1 or l2
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    p, q = l1, l2
    while p and q:
      val = carry + p.val + q.val
      if val >= 10:
        carry = 1
        val -= 10
      else:
        carry = 0
      cur.val = val
      if p.next or q.next:
        cur.next = ListNode(0)
        cur = cur.next
      p = p.next
      q = q.next
    l = p or q
    while l:
      val = carry + l.val
      if val >= 10:
        carry = 1
        val -= 10
      else:
        carry = 0
      if l.next:
        cur.next = ListNode(0)
        cur = cur.next
      l = l.next
    if carry == 1:
      cur.next = ListNode(carry)
    return dummy
