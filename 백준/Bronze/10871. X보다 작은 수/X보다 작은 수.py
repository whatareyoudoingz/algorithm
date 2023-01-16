n, v=map(int,input().split())
lis=list(map(int,input().split()))

print(" ".join(str(i) for i in lis if i < v))