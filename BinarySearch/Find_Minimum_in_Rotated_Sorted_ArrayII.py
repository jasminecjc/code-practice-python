# -*- coding:utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.
'''
class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if nums[mid] == nums[end]:
        end = end -1
      elif nums[mid] < nums[end]:
        end = mid
      else:
        start = mid
    if nums[start] <= nums[end]:
      return nums[start]
    return nums[end]