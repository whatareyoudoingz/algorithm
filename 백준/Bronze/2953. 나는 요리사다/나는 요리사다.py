score={}
for i in range(5):
    score[i]=sum(map(int,input().split()))

for x,y in score.items():
    if y == max(score.values()):
        print(x+1,y)