# -*- coding:utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
  def twoSum(self, nums, target):
    hashmap = {}
    for idx, val in enumerate(nums):
      if hashmap.has_key(target - val):
        return [hashmap(target - val), idx]
      else:
        hashmap[val] = idx
    return [-1, -1]