N=int(input())
A=[[0,0] for _ in range(N)]

for i in range(N):
    s,e=map(int,input().split())
    A[i][0]=e
    A[i][1]=s
A.sort()
cnt=0
end=0
for i in range(N):
    if A[i][1]>=end:
        cnt+=1
        end=A[i][0]
print(cnt)