# -*- coding:utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
'''
class Solution:
  def gen(self, left, right, solution, res):
    if left > right:
      return
    if left == 0 and right == 0:
      res.append(solution)
      return
    if left > 0:
      self.gen(left - 1, right, solution + '(', res)
    if right > 0:
      self.gen(left, right - 1, solution + ')', res)
  def generate(self, n):
    res = []
    if n <= 0:
      return res
    self.gen(n, n, '', res)
    return res
    