n=int(input())
number=list(map(int,input()))

total, i=0, 0
while i!=n:
    total+=number[i]
    i+=1

print(total)