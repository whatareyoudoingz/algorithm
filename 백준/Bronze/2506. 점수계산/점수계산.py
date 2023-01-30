n=int(input())
array=list(map(int,input().split()))

for i in range(n):
    if i == 0 :
        continue
    if array[i] == 1:
        if array[i-1] != 0 :
            array[i] = array[i-1]+1
print(sum(array))