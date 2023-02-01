n,m=map(int,input().split())
number=list(input().split())

max=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tot=int(number[i])+int(number[j])+int(number[k])
            if max <  tot and tot <= m:
                max=tot
print(max)