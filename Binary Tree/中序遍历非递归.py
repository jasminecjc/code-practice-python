# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeToSequence:
    def inOrder(self, root):
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        cur = root
        while len(stack) or cur:
            while cur.left:
                stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
