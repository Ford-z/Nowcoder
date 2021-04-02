#作者：一只酷酷熊
#链接：https://www.nowcoder.com/discuss/612463
#来源：牛客网

#题意

#一个长度为 nn 的 01 串，要把串变成某个位置左边全是 1 ，右边全是 0 至少要修改几个字符

#分析

#我们不知道应该把串变成几个 1 几个 0 ，考虑枚举 1 和 0 的分界点

#设串的下标为 [1, n] ，枚举的分界点为 ii，令 [1, i] 全部为 1，[i + 1, n] 全部为 0

#把 [1, i] 这个区间内的数全变成 1 的次数等于这个区间内 0 的个数

#把 [i + 1, n] 这个区间内的数全变成 0 的次数等于这个区间 1 的个数

#可以预处理前缀和 sum[i] 为 [1, i] 中 1 的个数，然后就可以在 O(1) 的时间复杂度内求出每个分界点要变化的数的个数，更新答案即可

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    line = str(sys.stdin.readline().strip())
        # 把每一行的数字分隔后转化成int列表
    r=0
    b=0
    tmp=[0]*(n+1)
    for i in range(1,n+1):
        tmp[i]=tmp[i-1]+int(line[i])
    ans=0
    for i in range(0,n+1):
    # [1, i]中'0'的个数为 i - sum[i]
    # [i + 1, n]中'1'的个数为 sum[n] - sum[i]
        ans=min(ans,i-tmp[i]+tmp[n]-tmp[i])
    print ans
