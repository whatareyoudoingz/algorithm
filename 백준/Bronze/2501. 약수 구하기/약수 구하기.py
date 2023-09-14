n,k=map(int,input().split())
result=[]
for i in range(1,n+1):
    if n%i==0 and n//i not in result:
        result.append(n//i)
print(0 if len(result)<k else result[-k])