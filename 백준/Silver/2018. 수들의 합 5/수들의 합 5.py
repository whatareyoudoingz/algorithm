n=int(input())
count=1
start=1
end=1
s=1
while end != n:
    if s == n:
        end+=1
        s+=end
        count+=1
    elif s > n:
        s-=start
        start+=1
    else:
        end+=1
        s+=end
print(count)