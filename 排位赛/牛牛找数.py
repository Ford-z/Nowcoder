#链接：https://ac.nowcoder.com/acm/contest/9976/A
#来源：牛客网

#牛牛有两个数a和b，他想找到一个大于a且为b的倍数的最小整数，只不过他算数没学好，不知道该怎么做，现在他想请你帮忙。
#给定两个数a和b，返回大于a且为b的倍数的最小整数。

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 给定两个数a和b，返回大于a且为b的倍数的最小整数。​
# @param a int整型 代表题目中描述的a
# @param b int整型 代表题目中描述的b
# @return int整型
#
class Solution:
    def solve(self , a , b ):
        # write code here
        c=a%b
        c=b-c
        return a+c
