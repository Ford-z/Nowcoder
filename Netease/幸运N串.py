#小A很喜欢字母N，他认为连续的N串是他的幸运串。有一天小A看到了一个全部由大写字母组成的字符串，他被允许改变最多2个大写字母（也允许不改变或者只改变1个大写字母），使得字符串中所包含的最长的连续的N串的长度最长。你能帮助他吗？

number = input()
for i in range(int(number)):
    a = input()
    b=[]
    if(len(a) - a.count("N") <=2):
        print(len(a))
    else:
        c = 0
        for t in range(len(a)):
            b.append(a[t])
            if len(b) - b.count('N') >= 3:
                b.pop(0)
            c=max(c,len(b))
        print(c)
