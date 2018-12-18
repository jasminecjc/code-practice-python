# -*- coding:utf-8 -*-
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
解析:最坏情况下需要遍历 n+n−1+...+1=O(n2) n + n - 1 + ... + 1 = O(n^2)n+n−1+...+1=O(n2), 平均情况下 n+n/2+n/4+...+1=O(2n)=O(n)n + n/2 + n/4 + ... + 1 = O(2n)=O(n)n+n/2+n/4+...+1=O(2n)=O(n). 故平均情况时间复杂度为 O(n). 交换数组的值时使用了额外空间，空间复杂度 O(1).
'''
class Solution:
  def findKthLargest(self, nums, k):
    if not nums or k < 1 or k > len(nums):
      return None
    return self.partition(nums, 0, len(nums) - 1, len(nums) -k)
  
  def partition(self, nums, start, end, k):
    if start == end:
      return nums[k]
    low, high = start, end
    pivot = nums[(low + high) // 2]
    while low <= high:
      while low <= high and nums[low] < pivot:
        low += 1
      while low <= high and nums[high] > pivot:
        high -= 1
      if low <= high:
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low + 1, high - 1
    if k <= high:
      return self.partition(nums, start, high, k)
    if k >= low:
      return self.partition(nums, low, end, k)
    return nums[k]

arr = [3,21,7,5,1,9,3,2]
k = 1
test = Solution()
print(test.findKthLargest(arr, k))