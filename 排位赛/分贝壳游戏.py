#链接：https://ac.nowcoder.com/acm/contest/9752/C
#来源：牛客网

#现在牛牛和牛妹一起出去海滩游玩，由于他们两个都不会游泳，所以他们在海滩捡了很多好看的贝壳，可是捡着捡着他们就感觉无聊了，所以他们决定拿这些贝壳玩一些游戏。
#他们一共捡了n个贝壳，现在他们这n个贝壳放成一堆。然后轮流取贝壳，牛牛先取。牛牛一次能取[1,p]个贝壳，牛妹一次能取[1,q]个贝壳,能拿到最后一个贝壳的人赢
#问牛牛和牛妹都足够聪明的情况下，最后谁能取得胜利
#如果牛牛必胜，返回1
#如果牛妹必胜，返回-1
#如果没有人有必胜策略，返回0
#p=q:
#n%(p+1)==0 牛妹胜
#n%(p+1)!=0 牛牛胜
#p>q:
#n<=p 牛牛胜，一步取完
#n=p+1 牛牛先取一个无论牛妹取多少，牛牛都能一步取完
#n>=p+1 无论如何n都会到n<=p+1，且牛妹取不走那种
#p<q
#n<=p 牛牛胜，一步取完
#其他情况牛妹胜
# 
# @param n int整型 
# @param p int整型 
# @param q int整型 
# @return int整型
#
class Solution:
    def Gameresults(self , n , p , q ):
        # write code here
        if p>=n:
            return 1
        if p==q:
            if(n%(q+1)!=0):
                return 1
            else:
                return -1
        elif p>q:
            return 1
        return -1
