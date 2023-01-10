n=int(input())
number=list(map(int,input().split()))
m=max(number)
number=[i/m*100 for i in number]
print(sum(number)/len(number))