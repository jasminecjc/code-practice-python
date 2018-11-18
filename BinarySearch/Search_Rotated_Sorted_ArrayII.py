# -*- coding:utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.
'''
class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    if len(nums) == 0:
      return False
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] == target:
        return True
      if nums[mid] == nums[end]:
        end = end -1
      elif nums[mid] < nums[end]:
        if nums[mid] < target and target <= nums[end]:
          start = mid
        else:
          end = mid
      else:
        if nums[mid] > target and target >= nums[start]:
          end = mid
        else:
          start = mid
    if nums[start] == target:
      return True
    if nums[end] == target:
      return True
    return False