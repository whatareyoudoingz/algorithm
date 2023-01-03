a,b,c=map(int,input().split())

#### 이중괄호 주의!!!!!
x=(a+b)%c
y=((a%c)+(b%c))%c
z=(a*b)%c
q=((a%c)*(b%c))%c

for i in [x,y,z,q]:
	print(i)