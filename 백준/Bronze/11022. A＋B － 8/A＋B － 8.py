import sys

T=int(input())
for i in range(T):
    b,c=map(int,sys.stdin.readline().split())
    print(f"Case #{i+1}: {b} + {c} = {b+c}")