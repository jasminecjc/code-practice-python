'''
题目: 如果对于一个字符串A，将A的前面任意一部分挪到后边去形成的字符串称为A的旋转词。
比如A="12345",A的旋转词有"12345","23451","34512","45123"和"51234"。对于两
个字符串A和B，请判断A和B是否互为旋转词。
给定两个字符串A和B及他们的长度lena，lenb，请返回一个bool值，代表他们是否互为旋转词。
'''
# -*- coding:utf-8 -*-


class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        if(lena == lenb and B in A + A):
            return True
        return False
