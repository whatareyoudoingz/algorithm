n=int(input())
result=sorted(list(map(int,input().split())))
for i in range(len(result)-1):
    result[i+1]+=result[i]
print(sum(result))