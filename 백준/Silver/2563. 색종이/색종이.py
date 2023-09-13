ans=[[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            ans[a+i][b+j]=1
result=0      
for x in range(100):
    for y in range(100):
        if ans[x][y]==1:
            result+=1
print(result)