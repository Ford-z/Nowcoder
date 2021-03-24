#将给出的32位整数x翻转。
#例1:x=123，返回321
#例2:x=-123，返回-321

#你有注意到翻转后的整数可能溢出吗？因为给出的是32位整数，则其数值范围为[−2^{31}, 2^{31} − 1]。翻转可能会导致溢出，如果反转后的结果会溢出就返回 0。

#
# 
# @param x int整型 
# @return int整型
#
class Solution:
    def reverse(self , x ):
        # write code here
        x=list(str(x))
        ans=[]
        if x[0]=="-":
            ans.append(x[0])
            for i in range(len(x)-1,0,-1):
                ans.append(x[i])
        else:
            for i in range(len(x)-1,-1,-1):
                ans.append(x[i])
        return int("".join(ans))
