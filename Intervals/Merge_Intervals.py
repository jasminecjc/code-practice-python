# -*- coding:utf-8 -*-
'''
Given a collection of intervals, merge all overlapping intervals.
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
  def merge(self, intervals):
    intervals = sorted(intervals, key = lambda x: x.start)
    merge = []
    for interval in intervals:
      if not merge or merge[-1].end < interval.start:
        merge.append(interval)
      else:
        merge[-1].end = max(merge[-1].end, interval.end)
    return merge