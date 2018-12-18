# -*- coding:utf-8 -*-
'''
Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def inorderTraversal(self, root):
    if not root:
      return []
    stack = res = []
    cur = root
    while len(stack) or cur:
      while cur:
        stack.append(cur)
        cur = cur.left
      cur = stack.pop()
      res.append(cur.val)
      cur = cur.right
    return res