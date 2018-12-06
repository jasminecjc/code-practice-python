# -*- coding:utf-8 -*-
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
'''
class Solution(object):
  def threeSum(self, nums):
    nums = sorted(nums)
    res = []
    for idx, val in enumerate(nums):
      if idx and val == nums[i - 1]:
        continue
      l, r = idx + 1, len(nums) - 1
      while l < r:
        ans = nums[l] + nums[r]
        if ans == -val:
          res.append([val, nums[l], nums[r]])
          while l < r and nums[l] == nums[l - 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          l += 1
          r -= 1
        elif ans < -val:
          l += 1
        else:
          r -= 1 
    return res

test = Solution()
arr = [-1,0,1,2,-3,-1,-1,3]
print(test.threeSum(arr))