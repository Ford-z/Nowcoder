#链接：https://ac.nowcoder.com/acm/contest/10324/A
#来源：牛客网

#若一个数的首位和末位相等，则定义这个数为“好数”。
#例如：1231、4512394是好数，而12345、768740则不是好数。
#请你编写一个函数，判断是不是好数。如果是好数则返回true，否则返回false。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 判断x是不是好数
# @param x int整型 待判断的数
# @return bool布尔型
#
class Solution:
    def judge(self , x ):
        # write code here
        x=str(x)
        a=list(x)
        if(a[0]==a[-1]):
            return True
        else:
            return False
