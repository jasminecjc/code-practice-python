# -*- coding:utf-8 -*-
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''
class Solution:
  def findDuplicate(self, nums):
    low, high = 1, len(nums) - 1
    while low < high:
      mid = (low + high) // 2
      for i in nums:
        count += 1 if i <= mid else 0
      if count > mid:
        high = mid
      else:
        low = mid + 1
    return low