class Solution(object):
    def myAtoi(self, str):
      """
      :type str: str
      :rtype: int
      """
      if len(str) == 0:
        return 0
      low, high = 0, len(str) - 1
      sign = 1
      num = 0
      max_num = 2147483648
      
      while low < high and str[low] == ' ':
        low += 1
      if str[low] == '-':
        sign = -1
        low += 1
      elif str[low] == '+':
        low += 1
      else:
        pass
      while low <= high:
        if str[low] >= '0' and str[low] <= '9':
          digit = ord(str[low]) - ord('0')
          num = digit + num * 10
          if num >= max_num:
            num = max_num if sign == -1 else max_num - 1
            break
          low += 1
        else:
          break
      return num * sign
test = Solution()
str = ' '
print(test.myAtoi(str))