for _ in range(int(input())):
    string, lis, i =input(), [], 0
    while i != len(string):
        if string[i] == '(':
            lis.append(string[i])
        else:
            if '(' in lis:
                lis.pop()
            else:
                break
        i+=1
    if i == len(string) and len(lis)==0:
        print("YES")
    else:
        print("NO")