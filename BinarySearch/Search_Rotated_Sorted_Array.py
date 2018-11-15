# -*- coding:utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
'''

class Solution:
  def search(self, nums, target):
    if len(nums) == 0:
      return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] == target:
        return mid
      if nums[mid] < nums[end]:
        if target > nums[mid] and target <= nums[end]:
          start = mid
        else:
          end = mid
      if nums[mid] > nums[start]:
        if target < nums[mid] and target >= nums[start]:
          end = mid
        else:
          start = mid
    if nums[start] == target:
      return start
    if nums[end] == target:
      return end
    return -1

test = Solution()
nums = [4,5,6,7,0,1,2]
target = 4
print(test.search(nums, target))