# -*- coding:utf-8 -*-
'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
'''
class Solution:
  def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    if len(arr) == 0:
      return []
    index = self.findTargetIndex(arr, x)
    if index == 0:
      return arr[0: k]
    if index == len(arr):
      return arr[-k:]
    start, end = index - 1, index
    while k > 1:
      k = k - 1
      if start <= 0:
        end = end + 1
      elif end >= len(arr):
        start = start - 1
      elif x - arr[start] <= arr[end] - x:
        start = start - 1
      else:
        end = end + 1
    return arr[start: end]


  def findTargetIndex(self, arr, x):
    if x <= arr[0]:
      return 0
    if x >= arr[len(arr) - 1]:
      return len(arr)
    start, end = 0, len(arr) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if arr[mid] == x:
        return mid
      elif arr[mid] < x:
        start = mid
      else:
        end = mid
    if arr[start] < x:
      return start + 1
    if arr[end] > x:
      return end
    
test = Solution()
arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
print(test.findClosestElements(arr, k, x))