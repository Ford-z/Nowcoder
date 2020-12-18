#链接：https://ac.nowcoder.com/acm/contest/10166/C
#来源：牛客网

#牛牛最近学会了异或操作，于是他发现了一个函数f(x)=x\oplus (x-1)f(x)=x⊕(x−1)，现在牛牛给你一个数\mathit nn，他想知道\sum_{i=1}^n f(i)∑ 
#i=1
#n
#​	
# f(i)的值是多少，请你告诉他。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n int整型 
# @return long长整型
#
class Solution:
    def Sum(self , n ):
        # write code here
        res=0
        flag=1
        while n:
            res=res+n*flag
            n=n//2
            flag=flag*2
        return res
