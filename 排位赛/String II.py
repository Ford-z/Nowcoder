#链接：https://ac.nowcoder.com/acm/contest/9715/B
来源：牛客网

给出一个仅包含小写字母的字符串s，你最多可以操作k次，使得任意一个小写字母变为与其相邻的小写字母（ASCII码差值的绝对值为1），请你求出可能的最长相等子序列（即求这个字符串修改至多k次后的的一个最长子序列，且需要保证这个子序列中每个字母相等）。
#
# 
# @param k int整型 表示最多的操作次数
# @param s string字符串 表示一个仅包含小写字母的字符串
# @return int整型
#
class Solution:
    def string2(self , k , s ):
        # write code here
        b=[ord(i) for i in "qwertyuiopasdfghjklzxcvbnm"]
        a=[]
        ans=0
        for x in s:
            a.append(ord(x))
        for x in b:
            t=k
            q=[]
            for i in a:
                q.append(abs(i-x))
            q.sort()
            j=0
            while(t>0 and j<len(q)):
                if(t>=q[j]):
                    t-=q[j]
                    j+=1
                else:
                    break
            ans=max(ans,j)
        return ans
