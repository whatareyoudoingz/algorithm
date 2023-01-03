n1=int(input())
n2=int(input())

t=0
result=0
for i in str(n2)[::-1]:
	answer=n1*int(i)
	print(answer)
	result+=(10**(t))*answer
	t+=1

print(result)