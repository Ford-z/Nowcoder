#链接：https://ac.nowcoder.com/acm/contest/9556/A
#来源：牛客网
#给你一个含有n个元素的数组arr[i]，请你告诉牛牛这个数组的中位数大还是平均数大，如果中位数更大输出1，如果平均数更大输出-1，如果中位数和平均数相等输出0

#
# 
# @param arr int整型一维数组 
# @return int整型
#
class Solution:
    def Answerofjudge(self , arr ):
        # write code here
        a=sum(arr)/len(arr)
        arr.sort()
        if(len(arr)%2==1):
            b=arr[(len(arr)-1)//2]
        else:
            b=arr[(len(arr))//2]+arr[(len(arr))//2-1]
            b/=2
        if(b>a):
            return 1
        elif(b==a):
            return 0
        elif(a>b):
            return -1
