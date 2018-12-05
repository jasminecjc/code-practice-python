# -*- coding:utf-8 -*-
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
class Solution:
  def moveZeroes(self, nums):
    left, right = 0, 0
    while right < len(nums):
      if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
      right += 1