space=[[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            space[x][y]=1

result=0
for i in range(len(space)):
    for j in range(len(space)):
        if space[i][j]==1:
            result+=1
print(result)