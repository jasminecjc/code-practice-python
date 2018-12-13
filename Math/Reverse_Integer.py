# -*- coding:utf-8 -*-
'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
class Solution:
  def reverse(self, x):
    if abs(x) < 10:
      return x
    boundary = 2 ** 31
    neg_boundary = -1 * boundary
    res = 0
    flag = 1 if x > 0 else -1
    x = abs(x)
    while x > 0:
      digit = x % 10
      x //= 10
      res = res * 10 + digit
    if res > boundary or res < neg_boundary:
      return 0
    return flag * res

test = Solution()
print(test.reverse(0))