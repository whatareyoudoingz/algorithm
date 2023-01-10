n=int(input())
for i in range(1,n+1):
    number=list(map(int,input().split()))
    print(f"#{i} {max(number)}")