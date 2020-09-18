#请实现有重复数字的有序数组的二分查找。输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一。
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#
class Solution:
    def upper_bound_(self , n , v , a ):
        # write code here
        t=min(n,v)
        b=a
        b.sort()
        ans=0
        if(b[-1]<t):
            return len(a)+1
        else:
            for i in range(len(a)):
                if(a[i]>=t):
                    ans=i+1
                    return ans
