#作者：一只酷酷熊
#链接：https://www.nowcoder.com/discuss/612463
#来源：牛客网

#题意

#三个人各自拥有一个字符串，他们的字符串长度相等，游戏进行 nn 回合，每回合每个人必须修改自己字符串中的一个字母，每个人最终得分是他字符串中出现次数最多的字母数量，判断谁最终得分最多。

#分析

#有一个显而易见的贪心策略是先找到出现最多的字母是哪个，然后把其他字母尽可能都改成这个字母

#设出现次数最多的字母数量是 x ，再进行 n 回合，这个字母就可以有 min(x + n, len) 个

#如果 x + n > len 不必担心在全部改成同一个字母之后每回合还必须改掉一个

#可以留一个字母先改成其他字母，在最后一回合再改成目标字母即可


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    s1 = str(sys.stdin.readline().strip())
    s2 = str(sys.stdin.readline().strip())
    s3 = str(sys.stdin.readline().strip())
    m=len(s1)
    a=s1.count(max("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",key=s1.count))+n
    b=s2.count(max("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",key=s2.count))+n
    c=s3.count(max("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",key=s3.count))+n
    x=min(a,m)
    y=min(b,m)
    z=min(c,m)
    if x > y and x > z:
        print "xiaoming"
    elif y > x and y > z:
        print "xiaowang"
    elif z > x and z + y:
        print "xiaoli"
    else:
        print "draw"
