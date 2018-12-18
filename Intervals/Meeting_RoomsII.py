# -*- coding:utf-8 -*-
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''
class Solution:
  def minMeetingRooms(self, intervals):
    if len(intervals) == 0:
      return 0
    temp = []
    for i in intervals:
      temp.append((i.start, 1))
      temp.append((i.end, -1))
    temp = sorted(temp, key = lambda v: (v[0], v[1]))
    n = max_num = 0
    for j in temp:
      n += j[1]
      max_num = max(max_num, n)
    return max_num