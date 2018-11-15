# -*- coding:utf-8 -*-
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
  def searchRange(self, nums, target):
    res = [-1, -1]
    if len(nums) == 0 or nums[0] > target or nums[len(nums) - 1] < target:
      return res
    if nums[0] == nums[len(nums) - 1] == target:
      return [0, len(nums) - 1]
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] == target:
        res = [mid, mid]
        while start + 1 < res[0]:
          smid = start + (res[0] - start) // 2
          if nums[smid] == target:
            res[0] = smid
          else:
            start = smid
        if nums[start] == target:
          res[0] = start
        start = res[0]
        while res[1] + 1 < end:
          emid = res[1] + (end - res[1]) // 2
          if nums[emid] == target:
            res[1] = emid
          else:
            end = emid
        if nums[end] == target:
          res[1] = end
        end = res[1]
        break
      elif nums[mid] < target:
        start = mid
      else:
        end = mid
    if nums[start] == target and nums[end] == target:
      res = [start, end]
    elif nums[start] == target:
      res = [start, start]
    elif nums[end] == target:
      res = [end, end]
    else:
      pass
    return res
          
test = Solution()
nums = [1,2,2,3,4,4,4]
target = 4
print(test.searchRange(nums, target))