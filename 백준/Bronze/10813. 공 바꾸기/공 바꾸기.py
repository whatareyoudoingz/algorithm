n,m=map(int,input().split())
ans=[i for i in range(1,n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    ans[a-1],ans[b-1]=ans[b-1],ans[a-1]
print(" ".join(str(j) for j in ans))