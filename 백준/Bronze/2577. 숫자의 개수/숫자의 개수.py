answer=1
for _ in range(3):
    answer*=int(input())
for i in range(10):
    print(str(answer).count(str(i)),sep='\n')