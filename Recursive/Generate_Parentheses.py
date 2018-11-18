# -*- coding:utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
'''
class Solution:
  def helper(self, n, res):
    if n == 0
      return []
    res.push('()')
    self.helper(n - 1, res)
  def generate(self, n):
    res = []
    if n == 0:
      return res
    return self.helper(self, n, res)
    