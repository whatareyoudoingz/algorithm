n,b = map(int,input().split())
result=[]
while True:
    if n==0:
        break
    if 10<=n%b:
        result.append(chr(n%b+55))
    else:
        result.append(str(n%b))
    n//=b
print(''.join(reversed(result)))