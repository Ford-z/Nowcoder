#给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
#
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s ):
        if(len(s)==0):
            return True
        a=[]
        flag=False
        # write code here
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                a.append(s[i])
            else:
                if (len(a)==0):
                    flag=False
                else:
                    if(s[i]==")" and a[-1]=="("):
                        a.pop()
                        flag=True
                    elif(s[i]=="}" and a[-1]=="{"):
                        a.pop()
                        flag=True
                    elif(s[i]=="]" and a[-1]=="["):
                        a.pop()
                        flag=True
                    else:
                        flag=False
        if(len(a)!=0):
            flag=False
        return flag
