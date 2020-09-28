#把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if(index==0):
            return 0
        dp=[0]*index
        dp[0]=1
        a=0
        b=0
        c=0
        for i in range(1,index):
            dp[i]=min(min(dp[a]*2,dp[b]*3),dp[c]*5)
            if(dp[i]/dp[a]==2):
                a+=1
            if(dp[i]/dp[b]==3):
                b+=1
            if(dp[i]/dp[c]==5):
                c+=1
        return dp[-1]
