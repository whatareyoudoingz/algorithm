for _ in range(int(input())):
    lis=input()
    come=[]
    score=0
    total_score=0
    for i in lis:
        come.append(i)
        if i=='O' and come[-1]==i:
            score+=1
        else:
            score=0
        total_score+=score

    print(total_score)