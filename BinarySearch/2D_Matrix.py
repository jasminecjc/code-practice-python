# -*- coding:utf-8 -*-
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
class Solution:
  def search(self, matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return False
    if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
      return False
    start = 0
    end = len(matrix) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if matrix[mid][0] == target:
        return True
      elif matrix[mid][0] > target:
        end = mid - 1
      else:
        start = mid
    if matrix[start][len(matrix[0]) - 1] < target:
      row = end
    else:
      row = start
    left = 0
    right = len(matrix[0]) - 1
    while left + 1 < right:
      mid = left + (right - left) // 2
      if matrix[row][mid] == target:
        return True
      elif matrix[row][mid] > target:
        right = mid
      else: 
        left = mid
    if matrix[row][left] == target:
      return True
    if matrix[row][right] == target:
      return True
    return False

matrix = [
  [1],[3]
]
target = 3
test = Solution()
print(test.search(matrix,target))