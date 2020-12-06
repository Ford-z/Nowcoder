#链接：https://ac.nowcoder.com/acm/contest/9715/C
#来源：牛客网
#音游狂热爱好者牛牛接到了一个新的任务，那就是给一张乐谱设计重音符。每当玩家敲击重音符的时候就会发出"bang"的美妙声音!!
#每一张乐谱都有nn个音符从左到右一字排开，现在牛牛的任务就是选出其中mm个音符将其标记为重音符，同时任意两个重音符之间都必须隔着至少kk个音符。
#一个有意思的问题诞生了，请求出这样合法的设计方案种数，并输出答案对10000000071000000007取模的结果。
#
# 
# @param n int整型 乐谱总音符数
# @param m int整型 重音符数
# @param k int整型 重音符之间至少的间隔
# @return long长整型
#
class Solution:
    def solve_bangbang(self , n , m , k ):
        # write code here
        if m==0:
            return 1
        dp=[[0]*(n+1) for i in range(m+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            dp[1][i]=1
        for i in range(2,m+1):
            for j in range(k+2,n+1):#因为j-k-1>=0
                dp[i][j]=(dp[i][j-1]+dp[i-1][j-k-1])%1000000007
        return sum(dp[m])%1000000007
