'''
题目:对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。
给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。
'''

# -*- coding: utf-8 -*-


class Parenthesis:
    def chkParenthesis1(self, A, n):
        res = []
        for i in A:
            if i == '(':
                res.append(i)
            elif i == ')':
                if len(res) and res[-1] == '(':
                    res.pop()
                else:
                    return False
            else:
                return False
        return False if len(res) else True

    def chkParenthesis2(self, A, n):
        num = 0
        for i in A:
            if i == '(':
                num += 1
            else if i == ')':
                num -= 1
            else:
                return False
            if num < 0:
                return False
        return False if num else True
