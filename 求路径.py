#一个机器人在m×n大小的地图的左上角（起点，下图中的标记“start"的位置）。机器人每次向下或向右移动。机器人要到达地图的右下角。（终点，下图中的标记“Finish"的位置）。可以有多少种不同的路径从起点走到终点？
# 
# @param m int整型 
# @param n int整型 
# @return int整型
#
class Solution:
    def uniquePaths(self , m , n ):
        # write code here
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
