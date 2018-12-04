# -*- coding:utf-8 -*-
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''

class Solution:
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0 or target <= nums[0]:
      return 0
    if target > nums[len(nums) - 1]:
      return len(nums)
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] == target:
        end = mid
      elif nums[mid] < target:
        start = mid
      else:
        end = mid
    if nums[end] >= target:
      return end
    if nums[start] <= target:
      return start + 1
    

test = Solution()
arr = arr = [0,1,1,1,2,3,6,7,8,9]
target = 1
print(test.searchInsert(arr, target))