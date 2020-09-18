#请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        a=[]
        for i in range(len(s)):
            if(s[i]==" "):
                a.append("%")
                a.append("2")
                a.append("0")
            else:
                a.append(s[i])
        str="".join(a)
        return str
