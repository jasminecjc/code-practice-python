class Solution:
  def find(self, prices):
    l, r = 0, len(prices) - 1
    max_profit = 0
    while l < r:
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        if max_profit < profit:
          max_profit = profit
        r -= 1
      else:
         l += 1
         r -= 1
    return max_profit

test = Solution()
arr = [7,6,5,4,3,10,2,8]
print(test.find(arr))