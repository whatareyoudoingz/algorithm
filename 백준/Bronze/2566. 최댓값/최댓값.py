answer=[]
max_ans,what=0,0
for i in range(9):
    ans=list(map(int,input().split()))
    max_ans=max(max_ans, max(ans))
    if max_ans == max(ans):
        what=i+1
        answer=ans
print(max_ans)
print(what, answer.index(max_ans)+1)