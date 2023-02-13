import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=[[0]*(n+1)] #원본 초기 리스트
D=[[0]*(n+1) for _ in range(n+1)] #구간 합 빈 리스트 #다이나믹 테이블

#원본 값 채우기
for i in range(n):
    A_row=[0]+list(map(int,input().split()))
    A.append(A_row)

#구간 합 리스트 채우기
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j]=D[i-1][j]+D[i][j-1]-D[i-1][j-1]+A[i][j]

#최종 답 구하기
for _ in range(m):
    s1,e1,s2,e2=map(int,input().split())
    print(D[s2][e2]-D[s1-1][e2]-D[s2][e1-1]+D[s1-1][e1-1])