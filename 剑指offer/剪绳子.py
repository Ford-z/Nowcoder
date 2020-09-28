#给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
class Solution:
    def cutRope(self, number):
        # write code here
        dp=[0]*(number+1)
        dp[number]=number
        for m in range(2,number):
            a=number//m
            t=number%m
            q=m-t
            dp[m]=pow(a,q)*pow(a+1,t)
        return max(dp)
