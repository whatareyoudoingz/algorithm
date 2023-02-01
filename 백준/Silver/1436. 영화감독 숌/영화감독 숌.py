T=int(input())
cnt, i=0, 666
while True:
    if '666' in str(i):
        cnt+=1
    if cnt == T:
        print(i)
        break
    i+=1