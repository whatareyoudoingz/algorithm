total=list(range(1,int(input())+1))
lis=[]
while len(total)!=1:
    lis.append(total.pop(0))
    total.append(total.pop(0))
print(*lis, total[0])