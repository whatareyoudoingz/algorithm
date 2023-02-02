T=int(input())
road=list(map(int,input().split()))

short, long=road[0], 0
i, ans=1, []
while True:
    if i==T:
        long=road[i-1] 
        h=long-short 
        ans.append(h)
        break
    if road[i]==road[i-1]: #평지 : 리셋
        short=road[i]
    if road[i]<road[i-1]: #내리막길
        long=road[i-1] 
        h=long-short 
        ans.append(h)
        short=road[i] 
    i+=1
print(max(ans))