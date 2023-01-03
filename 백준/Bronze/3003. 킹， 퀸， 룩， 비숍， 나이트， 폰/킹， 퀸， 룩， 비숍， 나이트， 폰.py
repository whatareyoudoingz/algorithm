inpu=list(map(int,input().split()))
one=[1,1,2,2,2,8]

i=0
for char in inpu:
	one[i]-=char
	i+=1

for i in one:
	print(i,end=' ')