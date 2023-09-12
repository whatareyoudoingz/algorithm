n,m=map(int,input().split())
ans=[list(map(int,input().split())) for _ in range(n*2)]
for i in range(n):
    for j in range(m):
        print(ans[i][j]+ans[i+n][j],end=" ")
    print()