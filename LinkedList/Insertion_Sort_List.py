# -*- coding:utf-8 -*-
'''
Sort a linked list using insertion sort.
Given 1->3->2->0->null, return 0->1->2->3->null.
'''
class Solution:
  def sort(self, head):
    if head == None or head.next == None:
      return head
    dummy = ListNode(0)
    while head != None:
      node = dummy.next
      while node.next != None and node.next.val < head.val:
        node = node.next
      temp = head.next
      head.next = node.next
      node.next = head
      head = temp
    return dummy.next