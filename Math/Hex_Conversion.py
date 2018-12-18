# -*- coding:utf-8 -*-
'''
Given a decimal number n and an integer k, Convert decimal number n to base-k.

1.0<=n<=2^31-1, 2<=k<=16
2.Each letter over 9 is indicated in uppercase
'''
class Solution:
  def hexConversion(self, n, k):
    if n == 0:
      return '0'
    res = ''
    while n > 0:
      temp = n % k
      digit = chr(ord('0') + temp) if temp < 10 else chr(ord('A') + (temp - 10))
      res = digit + res
      n = n // k
    return res