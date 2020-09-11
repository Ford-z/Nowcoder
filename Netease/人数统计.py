from collections import Counter
n,m = map(int,input().split())
salary = list(map(int,input().split()))
frequency_dict = dict(Counter(salary))
for i in(range(0,m)):
    question = int(input())
    a=frequency_dict.get(question)
    if(a==None):
        a=0
    print(a)
