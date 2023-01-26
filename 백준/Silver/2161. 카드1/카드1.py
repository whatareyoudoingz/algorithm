total=[i for i in range(1,int(input())+1)]
lis=[]
while len(total)!=1:
    lis.append(total[0])
    total.pop(0)
    t=total[0]
    total.pop(0)
    total.append(t)
print(" ".join(str(i) for i in lis+total))