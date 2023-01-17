s=input()
lis=[-1 for _ in range(26)]
for i in s:
    if lis[ord(i)-97] == -1 :
        lis[ord(i)-97] = s.find(i)
for a in lis:
    print(a , end=' ')