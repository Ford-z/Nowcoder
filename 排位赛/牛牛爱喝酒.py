#链接：https://ac.nowcoder.com/acm/contest/9752/A
#来源：牛客网

#牛牛是一个酒鬼，非常爱喝酒，一瓶酒m元钱，两个酒瓶可以换一瓶酒，四个瓶盖可以换一瓶酒，现在有 n 元钱，求最多可以喝多少瓶酒？
#（注：没有借贷功能，即最终不允许借一瓶酒、喝完后拿酒瓶兑换归还的操作）
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回牛牛能喝的最多的酒
# @param m int整型 酒单价
# @param n int整型 牛牛的现金
# @return int整型
#
class Solution:
    def countWine(self , m , n ):
        # write code here
        beer=n//m
        ans=beer
        btt, cap=beer,beer
        flag = 1
        while flag:
            a = btt//2 #酒瓶换酒
            b = cap//4 #瓶盖换酒
            tmp = a + b
            ans+=tmp
            if tmp > 0:
                btt = a + b + btt%2
                cap = a + b + cap%4
                flag = btt + cap
            else:
                flag=0
        return ans
