n,m=map(int,input().split())
ans=[]
for _ in range(n*2):
    ans.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if j==m-1:
            print(ans[i][j]+ans[i+n][j])
        else:
            print(ans[i][j]+ans[i+n][j],end=" ")