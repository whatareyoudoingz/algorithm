n,m=map(int,input().split())
ans=list(range(1,n+1))
for _ in range(m):
    a,b=map(int,input().split())
    result=ans[a-1:b]
    for i in range(a-1,b):
        ans[i]=result[-1]
        result.pop(-1)
print(*ans)