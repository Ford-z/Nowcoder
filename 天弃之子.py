#作者：一只酷酷熊
#链接：https://www.nowcoder.com/discuss/612463
#来源：牛客网

#题意

#游戏共有 nn 关，每一关有 a_i个按钮，其中只有一个可以过关，选择错误就会重新开始

#玩家可以通过试错记住正确的按钮

#问玩家运气最差时（每一关都要试 a_i次才过关）共需要按多少次按钮才能通关。

#分析

#这道题最重要的环节就是读懂题目

#从题意中分析出【每一关都要试 a_i次】之后就比较容易了

#对于每一关来说，都要进行 a_i - 1a次失败

#每次失败要先通过前面的 i - 1关，再算上当前这关，需要按 ii 次按钮

#所以往答案里累加 (a_i−1)⋅i

#再算上最终成功的那次，通过 nn 关需要按 nn 次按钮即可

class Solution:
    def findMaxButtons(self , buttons ):
        # write code here
        dp=[0]*len(buttons)
        dp[0]=buttons[0]
        for i in range(1,len(buttons)):
            dp[i]=1+(buttons[i]-1)*(i+1)
        return sum(dp)
