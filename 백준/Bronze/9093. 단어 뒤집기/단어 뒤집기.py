for _ in range(int(input())):
    s=list(input().split())
    answer=''
    for i in s:
        answer+=i[::-1]+" "
    print(answer)