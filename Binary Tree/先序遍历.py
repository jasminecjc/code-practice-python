# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeToSequence:
    def preOrder1(self, root, res):
        # 递归
        if not root:
            return []
        else:
            res.append(root.val)
            self.preOrder1(root.left, res)
            self.preOrder1(root.right, res)

    def preOrder2(self, root):
        # 非递归，用栈实现
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while len(stack):
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left
                stack.append(cur.left)
        return res
