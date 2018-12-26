class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs' ,'8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return res
        self.dfs(0, digits, mapping, '', res)
        return res
    def dfs(self, cur, digits, mapping, subset, res):
        if cur == len(digits):
            res.append(subset)
            return
        arr = mapping[digits[cur]]
        for i in range(len(arr)):
            subset += arr[i]
            self.dfs(cur + 1, digits, mapping, subset, res)
            subset = subset[0: len(subset) - 1]