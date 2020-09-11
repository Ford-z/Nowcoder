T = int(input())
for _ in range(T):
    x,y,z = map(int,input().split())
    food = [x,y,z]
    if((sum(food)-max(food))>max(food)//2):
        print((sum(food)+2)//3)
    else:
        print((max(food)+1)//2)
