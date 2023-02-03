answer=''
for a in range(10):
    n=int(input())
    string, lis , i=input() , [], 0
    dic={']':'[',')':'(','}':'{','>':'<'}
    while i != n:
        if string[i] in dic.values(): lis.append(string[i]) 
        else: #닫힌 괄호면
            if dic[string[i]] == lis[-1]: lis.pop()
            else: break
        i+=1
    if i == n and len(lis)==0:answer=1
    else: answer=0
    print(f"#{a+1} {answer}")