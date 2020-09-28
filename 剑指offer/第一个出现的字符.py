#在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
# -*- coding:utf-8 -*-
import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d3=collections.OrderedDict()
        for x in s:
            d3[x]=s.count(x)
        for (k,v) in  d3.items(): 
            if(v==1):
                return s.index(k)
        return -1
