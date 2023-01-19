import sys
n=int(input())
dic={}
for _ in range(n):
    name, active=sys.stdin.readline().split()
    if name not in dic:
        dic[name]=active
    else:
        dic.pop(name)
for word in sorted(dic.keys(),reverse=True):
    print(word)