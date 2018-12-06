# -*- coding:utf-8 -*-
'''
Implement pow(x, n), which calculates x raised to the power n (xn).
'''
class Solution:
  def myPow(self, x, n):
    flag = 1 if n < 0 else 0
    if flag:
      x = 1 / x
      n = -n
    return self.helper(x, n)
  
  def helper(self, x, n):
    if n == 0:
      return 1
    if n == 1:
      return x
    res = self.helper(x, n // 2)
    if n % 2 == 1:
      return res * res * x
    else:
      return res * res

test = Solution()
print(test.myPow(2, -2))
