n,k=map(int,input().split())
A=[int(input()) for _ in range(n)]
cnt=0
for i in range(n-1,-1,-1):
    if A[i] <= k:
        a=k//A[i]
        cnt+=a
        k=k%(A[i]*a)
print(cnt)