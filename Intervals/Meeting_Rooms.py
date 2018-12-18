# -*- coding:utf-8 -*-
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.
'''
class Solution:
  def canAttendMeetings(self, intervals):
    if len(intervals) == 0:
      return True
    intervals = sorted(intervals, key: lambda x: x.start)
    end = intervals[0].end
    for i in range(1, len(intervals)):
      if end > intervals[i].start:
        return False
      end = intervals[i].end
    return True