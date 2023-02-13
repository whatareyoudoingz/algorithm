import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
s=[0]*(n+1)
    
for i in range(1,n+1):  #구간합 코드 구현
    s[i]=s[i-1]+a[i]

for _ in range(m):
    start,end=map(int,input().split())
    print(s[end]-s[start-1])