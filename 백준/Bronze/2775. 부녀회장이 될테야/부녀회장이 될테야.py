T=int(input())
for _ in range(T):
    k, n=int(input()), int(input()) #층, 호
    storage=[[i for i in range(1,n+1)] for _ in range(k+1)]
    for x in range(1,k+1):
        for y in range(1,n):
            storage[x][y]=storage[x][y-1]+storage[x-1][y]
    print(storage[k][n-1])