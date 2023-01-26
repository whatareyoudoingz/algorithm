lis=[]
for _ in range(3):
    lis.append(int(input()))

dic={}
for i in set(lis):
    dic[i]=lis.count(i)

if sum(lis)==180:
    if len(dic.keys())==1:
        print("Equilateral")
    elif len(dic.keys())==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")