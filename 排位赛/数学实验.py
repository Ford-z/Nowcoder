#链接：https://ac.nowcoder.com/acm/contest/10166/A
#来源：牛客网

#牛牛在做数学实验。
#老师给了牛牛一个数字n，牛牛需要不断地将所有数位上的值做乘法运算，直至最后数字不发生变化为止。
#请你帮牛牛计算一下，最后生成的数字为多少？
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n long长整型 老师给牛牛的数字
# @return int整型
#
class Solution:
    def mathexp(self , n ):
        # write code here
        while(n>=10):
            a=str(n)
            a=list(a)
            n=1
            for i in range(len(a)):
                n=n*(int(a[i]))
        return n
