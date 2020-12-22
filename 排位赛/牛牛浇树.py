#链接：https://ac.nowcoder.com/acm/contest/10322/B
#来源：牛客网

#牛牛现在在花园养了n棵树，按顺序从第1棵到第n棵排列着。牛牛每天会按照心情给其中某一个区间的数浇水。例如如果某一天浇水的区间为[2,4]，就是牛牛在这一天会给第2棵，第3棵和第4棵树浇水。树被浇水后就会成长，为了简化问题，我们假设在初始时所有树的高度为0cm。每过去一天树会自然成长1cm，每次树被浇水后当天会额外成长1cm。m天中牛牛每天都都会选一个区间[l,r]对这个区间内的树进行浇水，牛牛想知道m天后有多少棵树的高度为奇数，你能告诉牛牛吗？
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回m天后高度为奇数的树的数量
# @param n int整型 
# @param m int整型 
# @param l int整型一维数组 
# @param r int整型一维数组 
# @return int整型
#
class Solution:
    def oddnumber(self , n , m , l , r ):
        # write code here
        ans=0
        dp = [0]*(n+10)
        for i in range(m):
            dp[l[i]]+=1
            dp[r[i]+1]-=1
        for i in range(1,n+1):
            dp[i]+=dp[i-1]
            if((dp[i]+m)%2==1):
                ans+=1
        return ans
