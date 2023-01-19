answer=[]
for _ in range(7):
    number=int(input())
    if number % 2 == 1 :
        answer.append(number)
if len(answer)==0:
    print(-1)
else:
    print(sum(answer), min(answer))