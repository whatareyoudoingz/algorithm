n,w=map(int,input().split()) #총 개수, 일수
nums=list(map(int,input().split())) #리스트
s=sum(nums[:w])
max_s=s
count=1

for end in range(w,n):
    start=end-w+1
    s=s-nums[start-1]+nums[end] #구간합
    
    if s>max_s: #새로운 최대구간값 발견
        max_s=s
        count=1
    elif s==max_s:
        count+=1
        
if max_s==0:
    print("SAD")
else:
    print(max_s)
    print(count)