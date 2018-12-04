class Solution:
  def quick_sort(self, arr):
    l, r = 0, len(arr) - 1
    while l <= r:
      if 