# -*- coding:utf-8 -*-
'''
解题步骤:
1. 异常处理
2. 边界条件
3. 二分缩小范围
4. 根据题目对start和end进行处理
'''

class Binary:
  def search(self, arr, target):
    if len(arr) == 0:
      return -1
    start = 0
    end = len(arr) - 1
    while start + 1 < end:
      mid = start + (end - start) // 2
      if target == arr[mid]:
        start = mid
      elif target < arr[mid]:
        end = mid
      else:
        start = mid 
    if arr[start] == target:
      return start
    if arr[end] == target:
      return end  
    return -1

arr = [1,2,2,3]
target = 2
test = Binary()
print(test.search(arr, target))