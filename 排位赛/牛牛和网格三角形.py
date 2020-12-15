#链接：https://ac.nowcoder.com/acm/contest/9976/C
#来源：牛客网

#牛牛有一个长和高都为为\mathit nn的网格三角形，牛牛想从从左下角点走到右上角点，但是牛牛只能向上或者向右沿着网格的边走，牛牛想知道从左下角点走到右上角点的方案数的奇偶性。牛牛现在给你\mathit nn，请你告诉牛牛路径方案数的奇偶性，若是奇数返回true，若是偶数返回false。

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n string字符串 三角形的长和高
# @return bool布尔型
#
import math
class Solution:
    def judge(self , n ):
        # 卡特兰数 C(2n,n)-C(2n,n-1)
        n=int(n)
        if(n==1):
            return True
        if(n==2):
            return False
        if(((2*n)&n)==n):
            if(((2*n)&(n-1))==(n-1)):
                return False
            else:
                return True
        else:
            if(((2*n)&(n-1))==(n-1)):
                return True
            else:
                return False
