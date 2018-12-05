# -*- coding:utf-8 -*-
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
class Solution:
  def plus(self, digits):
    digits = list(reversed(digits))
    digits[0] += 1
    i, carry = 0, 0
    while i < len(digits):
      digits[i] += carry
      if digits[i] >= 10:
        carry = 1
        digits[i] -= 10
      else:
        carry = 0
        break
      i += 1
    if i == len(digits) and carry == 1:
      digits.append(1)
    return list(reversed(digits))