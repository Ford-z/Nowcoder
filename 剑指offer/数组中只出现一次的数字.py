#一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        n=len(array)
        ans=[]
        t=2
        for i in range(n):
            a=array[0:i]+array[i+1:n]
            if array[i] not in a:
                ans.append(array[i])
                t-=1
                if(t==0):
                    break
        return ans
