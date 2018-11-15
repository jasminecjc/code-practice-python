# -*- coding:utf-8 -*-
'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''
class Solution:
  def sqrt(self, x):
    if x == 0 or x == 1:
      return x
    l, r = 1, x // 2
    while l + 1 < r:
      mid = l + (r - l) // 2
      if mid ** 2 < x and (mid + 1) ** 2 > x:
          return mid
      elif mid ** 2 < x:
          l = mid
      else:
          r = mid
    if r * r <= x and (r + 1)**2 > x:
        return r

test = Solution()
print(test.sqrt(17))