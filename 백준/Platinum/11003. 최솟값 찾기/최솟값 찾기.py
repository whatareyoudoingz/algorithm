from collections import deque #외우는 게 좋다!!!!!!
N,L=map(int,input().split())
nums=list(map(int,input().split()))
mydeque=deque()

for i in range(N):
    while mydeque and mydeque[-1][1]>nums[i]: 
        mydeque.pop()
    mydeque.append((i,nums[i]))
        
    if mydeque[0][0] < i-L+1:
        mydeque.popleft()
    print(mydeque[0][1],end=' ')