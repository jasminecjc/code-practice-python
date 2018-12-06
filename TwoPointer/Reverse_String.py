# -*- coding:utf-8 -*-
'''
Write a function that takes a string as input and returns the string reversed.
'''
class Solution:
  def reverse(self, s):
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
    return ''.join(s)
  
test = Solution()
print(test.reverse('a hamman:ojj man is, what.'))