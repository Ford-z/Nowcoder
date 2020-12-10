#给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
class Solution:
    def LIS(self , arr ):
        # write code here
        size=len(arr)
        if size <= 1:
            return arr
        dp=[1]*size
        for i in range(1,size):
            for j in range(i):
                if(arr[i]>arr[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        #a=max(dp)
        #q=dp.index(a)
        ans=[]
        #ans.append(q)
        for i in range(size-1,-1,-1):
            if len(ans)==0:
                ans.append(i)
            else:
                if dp[i]==dp[ans[-1]]-1:
                    ans.append(i)
                elif dp[i]==dp[ans[-1]] and arr[i]<arr[ans[-1]]:
                    ans.pop()
                    ans.append(i)
                elif dp[i]>dp[ans[0]]:
                    ans=[]
                    ans.append(i)
        res=[]
        for i in ans:
            res.append(arr[i])
        return res[::-1]
