# -*- coding:utf-8 -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
class Solution:
  def maxProfit(self, prices):
    if prices == None or len(prices) == 0:
      return 0
    low, high = sys.maxint, 0
    for i in prices:
      low = i if i < low else low
      high = i - low if i - low > high else high
    return high