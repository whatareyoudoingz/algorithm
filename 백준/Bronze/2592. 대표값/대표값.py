#2차원 리스트 이용하여 구현
number=[[0]*10 for _ in range(2)]
result=0
for i in range(10):
    n=int(input())
    result+=n
    if n not in number[0]:
        number[0][i]=n
        number[1][number[0].index(n)]=1
    else:
        number[1][number[0].index(n)]+=1
print(result//10, number[0][number[1].index(max(number[1]))],sep='\n')
