n=int(input())

total=0
for _ in range(n):
    string=input()
    dic=set(string[0])
    result=1
    for i in range(1,len(string)):
        if string[i] in dic:
            if string[ i-1] == string[i]:
                result+=1
                continue
            else:
                break
        else:
            dic.add(string[i])
            result+=1
    if result == len(string):
        total+=1
print(total)