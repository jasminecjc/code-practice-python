# -*- coding:utf-8 -*-
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def helper(self, root, level, res):
    if root:
      if len(res) < level + 1:
        res.append([])
      res[level].append(root.val)
      self.helper(root.left, level + 1, res)
      self.helper(root.right, level + 1, res)
  def levelOrder(self, root):
    if not root:
      return []
    res = []
    self.helper(root, 0, res)
    return res 
