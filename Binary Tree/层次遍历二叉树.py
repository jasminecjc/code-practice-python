'''
题目: 有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。
给定二叉树的根结点root，请返回打印结果，结果按照每一层一个数组进行储存，所有数组的顺序
按照层数从上往下，且每一层的数组内元素按照从左往右排列。保证结点数小于等于500。
'''
# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreePrinter:
    def printTree(self, root):
        res = []
        queue = []
        if(root == None):
            return res

        last = nlast = root
        temp = []
        queue.append(root)

        while(len(queue)):
            node = queue.pop(0)
            temp.append(node.val)

            if(node.left != None):
                queue.append(node.left)
                nlast = node.left

            if(node.right != None):
                queue.append(node.right)
                nlast = node.right

            if(node == last):
                res.append(temp[:])
                temp = []
                last = nlast

        return res
