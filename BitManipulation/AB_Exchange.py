class Solution:
  def swap(self, a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b