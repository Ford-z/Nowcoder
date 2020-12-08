#链接：https://ac.nowcoder.com/acm/contest/9752/B
#来源：牛客网

#牛牛现在有一个长度为len只包含小写字母‘a’-'z'的字符串x，他现在想要一个特殊的子序列，这个子序列的长度为3*n（n为非负整数），子序列的第[1,n]个字母全部为‘a’，子序列的[n+1,2*n]个字母全部为‘b’，子序列的[2*n+1,3*n]个字母全部为‘c’，牛牛想知道最长的符合条件的独特子序列的长度是多少。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param x string字符串 
# @return int整型
#
class Solution:
    def Maximumlength(self , x ):
        # write code here
        t=len(x)
        if(t==0):
            return 0
        else:
            left=0
            right=t
            ans=0
            while left<=right:
                mid=(left+right)//2
                if self.check(mid,x):
                    ans=mid
                    left=mid+1
                else:
                    right=mid-1
            return ans*3
    def check(self,mid,x):
        n=len(x)
        a=0
        b=0
        c=0
        for i in range(n):
            if a<mid:
                if x[i]=='a':
                    a+=1
            elif b<mid:
                if x[i]=='b':
                    b+=1
            elif c<mid:
                if x[i]=='c':
                    c+=1
        return c>=mid
