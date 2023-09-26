n,b=input().split()
result=0
for i in range(len(n),0,-1):
    if n[i-1].isdigit():
        result+=int(n[i-1]) * (int(b)**(len(n)-i))
    else:
        result+=(ord(n[i-1])-55) * (int(b)**(len(n)-i))
print(result)