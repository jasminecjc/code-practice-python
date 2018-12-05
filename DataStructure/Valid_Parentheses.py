# -*- coding:utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution:
  def isValid(self, s):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in a:
      if char in mapping:
        top = stack.pop() if stack else '#'
        if mapping[char] != top:
          return False
      else:
        stack.append(char)
    if stack:
      return False
    return True