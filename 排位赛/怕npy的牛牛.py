#链接：https://ac.nowcoder.com/acm/contest/9556/B
#来源：牛客网
#牛牛非常怕他的女朋友，怕到了走火入魔的程度，以至于每当他看到一个字符串同时含有n,p,y三个字母他都害怕的不行。现在有一个长度为m的只包含小写字母‘a’-‘z’的字符串x，牛牛想知道能令他不害怕的最长子串的长度是多少。（对于字符串”abc”来说，”c”,”ab”都是原串的子串，但”ac”不是原串子串）

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回符合题意的最长的子串长度
# @param x string字符串 
# @return int整型
#
class Solution:
    def Maximumlength(self , x ):
        # write code here
        n = x.split('n')
        p = x.split('p')
        y = x.split('y')
        ans=0
        for i in n:
            ans=max(ans,len(i))
        for i in p:
            ans=max(ans,len(i))
        for i in y:
            ans=max(ans,len(i))
        return ans
