# -*- coding:utf-8 -*-
'''
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).
You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
'''

class Solution(object):
  def search(self, reader, target):
    """
    :type reader: ArrayReader
    :type target: int
    :rtype: int
    """
    if target < reader.get(0):
      return -1
    index = 1
    while reader.get(index -1) < target:
      index = index * 2
    start, end = index / 2 - 1, index - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if reader.get(mid) == target:
        return mid
      elif reader.get(mid) > target:
        end = mid
      else:
        start = mid
    if reader.get(start) == target:
      return start
    if reader.get(end) == target:
      return end
    return -1