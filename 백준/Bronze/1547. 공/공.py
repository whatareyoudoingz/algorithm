ball=[0,1,2,3]
for _ in range(int(input())):
    a,b=map(int,input().split())
    x,y=ball.index(a), ball.index(b)
    ball[x],ball[y]=ball[y],ball[x]
print(ball[1])