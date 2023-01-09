a=int(input())
answer=[]
for i in range(a):
    n1,n2=map(int,input().split())
    answer.append(n1+n2)
for i in answer:
	print(i)