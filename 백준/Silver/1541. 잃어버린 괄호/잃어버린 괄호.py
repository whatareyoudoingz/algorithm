A=input().split('-')
B=[sum(map(int,i.split('+'))) for i in A]

answer=B[0]
for k in range(1,len(B)):
    answer-=B[k]
print(answer)