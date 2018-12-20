'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example:
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''
import numpy as np

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        temp = []
        res = np.zeros((len(nums)), dtype=np.int)
        while high >= low:
            cur = nums[high]
            left, right = 0, len(temp)
            while left < right:
                mid = (left + right) // 2
                if temp[mid] >= cur:
                    right = mid
                else:
                    left = mid + 1
            res[high] = left
            temp.insert(left, cur)
            high -= 1
            
        return res

test = Solution()
nums = [6,6]
print(test.countSmaller(nums))
