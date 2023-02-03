for a in range(10):
    n=int(input())
    number=list(map(int,input().split()))
    c=1
    while True:
        if c<0 or c==0:
            break
        for i in range(1,6):
            c=number[0]-i
            if c < 0 or c==0: 
                number.append(0)
                number.pop(0)
                break
            else:
                number.append(c)
                number.pop(0)

    print(f"#{a+1} "+" ".join(str(n) for n in number))