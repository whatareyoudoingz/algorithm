s=input()
lis=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lis:
    if i in s:
        s=s.replace(i," ")
print(len(s))