#链接：https://ac.nowcoder.com/acm/contest/9475/A
#来源：牛客网
#牛牛最近很喜欢掷硬币，由于他今天很无聊，所以他在家掷了n次硬币，如果这n次硬币全部朝上或者全部朝下牛牛就很开心，请问牛牛开心的概率是多少。（每次掷硬币朝上的概率与朝下的概率相同）
#
# 返回一个严格四舍五入保留两位小数的字符串
# @param n int整型 n
# @return string字符串
#
class Solution:
    def Probability(self , n ):
        # write code here
        a=pow(0.5,n)*2
        return ("%.2f" % (a+ 1e-7))
