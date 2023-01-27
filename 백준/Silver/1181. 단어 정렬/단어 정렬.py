lis=set(input() for _ in range(int(input())))
lis=sorted(sorted(lis,reverse=False),key= lambda x : len(x))
print(*lis, sep='\n')